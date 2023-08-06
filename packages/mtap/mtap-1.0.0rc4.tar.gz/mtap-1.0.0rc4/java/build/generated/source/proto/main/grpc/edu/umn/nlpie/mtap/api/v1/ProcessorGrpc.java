package edu.umn.nlpie.mtap.api.v1;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 * <pre>
 * A processor service is responsible for processing an event, adding results to
 * the events service, and then optionally returning a custom result.
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.52.1)",
    comments = "Source: mtap/api/v1/processing.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class ProcessorGrpc {

  private ProcessorGrpc() {}

  public static final String SERVICE_NAME = "mtap.api.v1.Processor";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest,
      edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse> getProcessMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Process",
      requestType = edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest,
      edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse> getProcessMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest, edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse> getProcessMethod;
    if ((getProcessMethod = ProcessorGrpc.getProcessMethod) == null) {
      synchronized (ProcessorGrpc.class) {
        if ((getProcessMethod = ProcessorGrpc.getProcessMethod) == null) {
          ProcessorGrpc.getProcessMethod = getProcessMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest, edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Process"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse.getDefaultInstance()))
              .setSchemaDescriptor(new ProcessorMethodDescriptorSupplier("Process"))
              .build();
        }
      }
    }
    return getProcessMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest,
      edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse> getGetInfoMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetInfo",
      requestType = edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest,
      edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse> getGetInfoMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest, edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse> getGetInfoMethod;
    if ((getGetInfoMethod = ProcessorGrpc.getGetInfoMethod) == null) {
      synchronized (ProcessorGrpc.class) {
        if ((getGetInfoMethod = ProcessorGrpc.getGetInfoMethod) == null) {
          ProcessorGrpc.getGetInfoMethod = getGetInfoMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest, edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetInfo"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse.getDefaultInstance()))
              .setSchemaDescriptor(new ProcessorMethodDescriptorSupplier("GetInfo"))
              .build();
        }
      }
    }
    return getGetInfoMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest,
      edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse> getGetStatsMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetStats",
      requestType = edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest,
      edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse> getGetStatsMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest, edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse> getGetStatsMethod;
    if ((getGetStatsMethod = ProcessorGrpc.getGetStatsMethod) == null) {
      synchronized (ProcessorGrpc.class) {
        if ((getGetStatsMethod = ProcessorGrpc.getGetStatsMethod) == null) {
          ProcessorGrpc.getGetStatsMethod = getGetStatsMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest, edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetStats"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse.getDefaultInstance()))
              .setSchemaDescriptor(new ProcessorMethodDescriptorSupplier("GetStats"))
              .build();
        }
      }
    }
    return getGetStatsMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static ProcessorStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ProcessorStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ProcessorStub>() {
        @java.lang.Override
        public ProcessorStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ProcessorStub(channel, callOptions);
        }
      };
    return ProcessorStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static ProcessorBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ProcessorBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ProcessorBlockingStub>() {
        @java.lang.Override
        public ProcessorBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ProcessorBlockingStub(channel, callOptions);
        }
      };
    return ProcessorBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static ProcessorFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ProcessorFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ProcessorFutureStub>() {
        @java.lang.Override
        public ProcessorFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ProcessorFutureStub(channel, callOptions);
        }
      };
    return ProcessorFutureStub.newStub(factory, channel);
  }

  /**
   * <pre>
   * A processor service is responsible for processing an event, adding results to
   * the events service, and then optionally returning a custom result.
   * </pre>
   */
  public static abstract class ProcessorImplBase implements io.grpc.BindableService {

    /**
     * <pre>
     * Processes an event.
     * </pre>
     */
    public void process(edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getProcessMethod(), responseObserver);
    }

    /**
     * <pre>
     * Gets information about the processor.
     * </pre>
     */
    public void getInfo(edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetInfoMethod(), responseObserver);
    }

    /**
     * <pre>
     * Gets globally-aggregated statistics about the processor.
     * </pre>
     */
    public void getStats(edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetStatsMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getProcessMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest,
                edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse>(
                  this, METHODID_PROCESS)))
          .addMethod(
            getGetInfoMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest,
                edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse>(
                  this, METHODID_GET_INFO)))
          .addMethod(
            getGetStatsMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest,
                edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse>(
                  this, METHODID_GET_STATS)))
          .build();
    }
  }

  /**
   * <pre>
   * A processor service is responsible for processing an event, adding results to
   * the events service, and then optionally returning a custom result.
   * </pre>
   */
  public static final class ProcessorStub extends io.grpc.stub.AbstractAsyncStub<ProcessorStub> {
    private ProcessorStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ProcessorStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ProcessorStub(channel, callOptions);
    }

    /**
     * <pre>
     * Processes an event.
     * </pre>
     */
    public void process(edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getProcessMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Gets information about the processor.
     * </pre>
     */
    public void getInfo(edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetInfoMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Gets globally-aggregated statistics about the processor.
     * </pre>
     */
    public void getStats(edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetStatsMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * <pre>
   * A processor service is responsible for processing an event, adding results to
   * the events service, and then optionally returning a custom result.
   * </pre>
   */
  public static final class ProcessorBlockingStub extends io.grpc.stub.AbstractBlockingStub<ProcessorBlockingStub> {
    private ProcessorBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ProcessorBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ProcessorBlockingStub(channel, callOptions);
    }

    /**
     * <pre>
     * Processes an event.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse process(edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getProcessMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Gets information about the processor.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse getInfo(edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetInfoMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Gets globally-aggregated statistics about the processor.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse getStats(edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetStatsMethod(), getCallOptions(), request);
    }
  }

  /**
   * <pre>
   * A processor service is responsible for processing an event, adding results to
   * the events service, and then optionally returning a custom result.
   * </pre>
   */
  public static final class ProcessorFutureStub extends io.grpc.stub.AbstractFutureStub<ProcessorFutureStub> {
    private ProcessorFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ProcessorFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ProcessorFutureStub(channel, callOptions);
    }

    /**
     * <pre>
     * Processes an event.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse> process(
        edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getProcessMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Gets information about the processor.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse> getInfo(
        edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetInfoMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Gets globally-aggregated statistics about the processor.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse> getStats(
        edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetStatsMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_PROCESS = 0;
  private static final int METHODID_GET_INFO = 1;
  private static final int METHODID_GET_STATS = 2;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final ProcessorImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(ProcessorImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_PROCESS:
          serviceImpl.process((edu.umn.nlpie.mtap.api.v1.Processing.ProcessRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.ProcessResponse>) responseObserver);
          break;
        case METHODID_GET_INFO:
          serviceImpl.getInfo((edu.umn.nlpie.mtap.api.v1.Processing.GetInfoRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.GetInfoResponse>) responseObserver);
          break;
        case METHODID_GET_STATS:
          serviceImpl.getStats((edu.umn.nlpie.mtap.api.v1.Processing.GetStatsRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.Processing.GetStatsResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class ProcessorBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    ProcessorBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return edu.umn.nlpie.mtap.api.v1.Processing.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Processor");
    }
  }

  private static final class ProcessorFileDescriptorSupplier
      extends ProcessorBaseDescriptorSupplier {
    ProcessorFileDescriptorSupplier() {}
  }

  private static final class ProcessorMethodDescriptorSupplier
      extends ProcessorBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    ProcessorMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (ProcessorGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new ProcessorFileDescriptorSupplier())
              .addMethod(getProcessMethod())
              .addMethod(getGetInfoMethod())
              .addMethod(getGetStatsMethod())
              .build();
        }
      }
    }
    return result;
  }
}
