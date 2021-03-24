# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pps import pps_pb2 as pps_dot_pps__pb2
from server.worker.server import service_pb2 as server_dot_worker_dot_server_dot_service__pb2


class WorkerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Status = channel.unary_unary(
        '/server.Worker/Status',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.WorkerStatus.FromString,
        )
    self.Cancel = channel.unary_unary(
        '/server.Worker/Cancel',
        request_serializer=server_dot_worker_dot_server_dot_service__pb2.CancelRequest.SerializeToString,
        response_deserializer=server_dot_worker_dot_server_dot_service__pb2.CancelResponse.FromString,
        )


class WorkerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Status(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Cancel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=pps_dot_pps__pb2.WorkerStatus.SerializeToString,
      ),
      'Cancel': grpc.unary_unary_rpc_method_handler(
          servicer.Cancel,
          request_deserializer=server_dot_worker_dot_server_dot_service__pb2.CancelRequest.FromString,
          response_serializer=server_dot_worker_dot_server_dot_service__pb2.CancelResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'server.Worker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))