# -*- coding: utf-8 -*-
#
# Copyright © 2020 NXP
# Copyright © 2020-2021 Chris Reed
# Copyright © 2023 IDEX Biometrics
#
# SPDX-License-Identifier: BSD-3-Clause
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the names of the copyright holders nor the names of the
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import logging
import grpc
from . import debugprobe_pb2_grpc, debugprobe_pb2

from time import sleep
from typing import Collection, List, Callable, Union

from pyocd.probe.debug_probe import DebugProbe
from pyocd.core.plugin import Plugin

from ._version import version as plugin_version

LOG = logging.getLogger(__name__)

TRACE = LOG.getChild("trace")
TRACE.disabled = True


class GrpcProbe(DebugProbe):
    """@brief Provides remote access to a debug probe using gRPC. """

    DEFAULT_PORT = 50051

    @classmethod
    def _extract_address(cls, unique_id):
        parts = unique_id.split(':', 1)
        if len(parts) == 1:
            port = cls.DEFAULT_PORT
        else:
            port = int(parts[1])
        return parts[0], port

    @classmethod
    def get_all_connected_probes(cls, unique_id=None, is_explicit=False):
        if is_explicit and unique_id is not None:
            return [cls(unique_id)]
        else:
            return []

    @classmethod
    def get_probe_with_id(cls, unique_id, is_explicit=False):
        return cls(unique_id) if is_explicit else None

    def __init__(self, unique_id):
        hostname,port = self._extract_address(unique_id)
        self._uid = f"{hostname}:{port}"
        self._channel = None
        self._stub = None
        self._open = False
        self._rpc_id = 0
        super().__init__()

    @property
    def _id(self) -> int:
        tmp = self._rpc_id
        self._rpc_id += 1
        return tmp

    @property
    def description(self) -> str:
        return "A remote gRPC debug probe"

    @property
    def vendor_name(self):
        return "pyOCD"

    @property
    def product_name(self):
        return "grpc_probe"

    @property
    def supported_wire_protocols(self):
        return [
            self.Protocol.DEFAULT,
            self.Protocol.SWD
        ]

    @property
    def unique_id(self):
        return f"remote_grpc:{self._uid}"

    @property
    def wire_protocol(self):
        return DebugProbe.Protocol.SWD 

    @property
    def is_open(self):
        return self._open

    @property
    def capabilities(self):
        return {
            self.Capability.SWJ_SEQUENCE,
            # self.Capability.SWD_SEQUENCE,
            # self.Capability.SWO, REVISIT: need to implement the SWO control methods
        }

    def open(self):
        self._channel = grpc.insecure_channel(self._uid)
        self._stub = debugprobe_pb2_grpc.DebugProbeServiceStub(self._channel)
        self._open = True

    def close(self):
        self._channel.close()
        self._open = False

    # --------------------------------------------------------------------------------
    # Target control
    # --------------------------------------------------------------------------------

    def connect(self) -> None:
        self._stub.DebugProbeCommand(
            debugprobe_pb2.DebugProbeRequest(
                id=self._id,
                command=debugprobe_pb2.Connect
            )
        )

    def disconnect(self) -> None:
        self._stub.DebugProbeCommand(
            debugprobe_pb2.DebugProbeRequest(
                id=self._id,
                command=debugprobe_pb2.Disconnect
            )
        )

    def set_clock(self, frequency: int) -> None:
        self._stub.DebugProbeCommand(
            debugprobe_pb2.DebugProbeRequest(
                id=self._id,
                command=debugprobe_pb2.SetClock,
                set_clock_req=debugprobe_pb2.SetClockRequest(frequency)
            )
        )

    def swj_sequence(self, length, bits) -> None:
        self._stub.DebugProbeCommand(
            debugprobe_pb2.DebugProbeRequest(
                id=self._id,
                command=debugprobe_pb2.SwjSequence,
                swj_seq_req=debugprobe_pb2.SwjSequenceRequest(
                    length=length,
                    bits=[
                        (bits >> i*64) & 0xffffffffffffffff 
                        for i in range((length+63)//64)
                    ]
                )
            )
        )


    # --------------------------------------------------------------------------------
    # DAP access
    # --------------------------------------------------------------------------------

    def read_dp(self, addr: int, now: bool=True) -> Union[int, Callable[[], int]]:
        values = self._read_reg(False, addr, 1)

        def read_cb():
            assert len(values) == 1
            return values[0]

        if now:
            return read_cb()
        else:
            return read_cb


    def write_dp(self, addr, value):
        self._write_reg(False, addr, [value])


    def read_ap(self, addr, now=True):
        values = self._read_reg(False, addr, 1)

        def read_cb():
            assert len(values) == 1
            return values[0]

        if now:
            return read_cb()
        else:
            return read_cb


    def write_ap(self, addr, value):
        self._write_reg(True, addr, [value])


    def read_ap_multiple(self, addr: int, count: int = 1, now: bool = True):
        values = self._read_reg(True, addr, count)

        def read_cb():
            assert len(values) == count
            return values

        if now:
            return read_cb()
        else:
            return read_cb


    def write_ap_multiple(self, addr: int, values: List[int]):
        self._write_reg(True, addr, values)


    def _read_reg(self, ap_n_dp: bool, addr: int, count: int):
        response = self._stub.DebugProbeCommand(
            debugprobe_pb2.DebugProbeRequest(
                id=self._id,
                command=debugprobe_pb2.ReadRegister,
                read_reg_req=debugprobe_pb2.ReadRegisterRequest(
                    ap_n_dp=ap_n_dp,
                    address=addr,
                    count=count
                )
            )
        )
        return response.values


    def _write_reg(self, ap_n_dp: bool, addr: int, values: List[int]) -> None:
        self._stub.DebugProbeCommand(
            debugprobe_pb2.DebugProbeRequest(
                id=self._id,
                command=debugprobe_pb2.WriteRegister,
                write_reg_req=debugprobe_pb2.WriteRegisterRequest(
                    ap_n_dp=ap_n_dp,
                    address=addr,
                    count=len(values),
                    values=values
                )
            )
        )



class GrpcProbePlugin(Plugin):
    """! @brief Plugin class for RemoteBitbangProbe."""

    def load(self):
        return GrpcProbe

    @property
    def name(self):
        return "remote_grpc"

    @property
    def description(self):
        return "remote gRPC debug probe"

    @property
    def version(self):
        return plugin_version

