package edu.umn.nlpie.mtap.api.v1;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 * <pre>
 * The events service, which stores Events (the top level discrete processing
 * objects a mapping of strings to Documents and strings to strings metadata),
 * Documents (a text string and a mapping of strings to LabelIndices), and
 * LabelIndices (collections of objects which mark locations in text having
 * some meaning).
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.52.1)",
    comments = "Source: mtap/api/v1/events.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class EventsGrpc {

  private EventsGrpc() {}

  public static final String SERVICE_NAME = "mtap.api.v1.Events";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse> getGetEventsInstanceIdMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetEventsInstanceId",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse> getGetEventsInstanceIdMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse> getGetEventsInstanceIdMethod;
    if ((getGetEventsInstanceIdMethod = EventsGrpc.getGetEventsInstanceIdMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetEventsInstanceIdMethod = EventsGrpc.getGetEventsInstanceIdMethod) == null) {
          EventsGrpc.getGetEventsInstanceIdMethod = getGetEventsInstanceIdMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetEventsInstanceId"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetEventsInstanceId"))
              .build();
        }
      }
    }
    return getGetEventsInstanceIdMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse> getOpenEventMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "OpenEvent",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse> getOpenEventMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse> getOpenEventMethod;
    if ((getOpenEventMethod = EventsGrpc.getOpenEventMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getOpenEventMethod = EventsGrpc.getOpenEventMethod) == null) {
          EventsGrpc.getOpenEventMethod = getOpenEventMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "OpenEvent"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("OpenEvent"))
              .build();
        }
      }
    }
    return getOpenEventMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse> getCloseEventMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "CloseEvent",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse> getCloseEventMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse> getCloseEventMethod;
    if ((getCloseEventMethod = EventsGrpc.getCloseEventMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getCloseEventMethod = EventsGrpc.getCloseEventMethod) == null) {
          EventsGrpc.getCloseEventMethod = getCloseEventMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "CloseEvent"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("CloseEvent"))
              .build();
        }
      }
    }
    return getCloseEventMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse> getGetAllMetadataMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetAllMetadata",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse> getGetAllMetadataMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse> getGetAllMetadataMethod;
    if ((getGetAllMetadataMethod = EventsGrpc.getGetAllMetadataMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetAllMetadataMethod = EventsGrpc.getGetAllMetadataMethod) == null) {
          EventsGrpc.getGetAllMetadataMethod = getGetAllMetadataMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetAllMetadata"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetAllMetadata"))
              .build();
        }
      }
    }
    return getGetAllMetadataMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse> getAddMetadataMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AddMetadata",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse> getAddMetadataMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse> getAddMetadataMethod;
    if ((getAddMetadataMethod = EventsGrpc.getAddMetadataMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getAddMetadataMethod = EventsGrpc.getAddMetadataMethod) == null) {
          EventsGrpc.getAddMetadataMethod = getAddMetadataMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AddMetadata"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("AddMetadata"))
              .build();
        }
      }
    }
    return getAddMetadataMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse> getAddDocumentMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AddDocument",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse> getAddDocumentMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse> getAddDocumentMethod;
    if ((getAddDocumentMethod = EventsGrpc.getAddDocumentMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getAddDocumentMethod = EventsGrpc.getAddDocumentMethod) == null) {
          EventsGrpc.getAddDocumentMethod = getAddDocumentMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AddDocument"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("AddDocument"))
              .build();
        }
      }
    }
    return getAddDocumentMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse> getGetAllDocumentNamesMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetAllDocumentNames",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse> getGetAllDocumentNamesMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse> getGetAllDocumentNamesMethod;
    if ((getGetAllDocumentNamesMethod = EventsGrpc.getGetAllDocumentNamesMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetAllDocumentNamesMethod = EventsGrpc.getGetAllDocumentNamesMethod) == null) {
          EventsGrpc.getGetAllDocumentNamesMethod = getGetAllDocumentNamesMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetAllDocumentNames"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetAllDocumentNames"))
              .build();
        }
      }
    }
    return getGetAllDocumentNamesMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse> getGetDocumentTextMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetDocumentText",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse> getGetDocumentTextMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse> getGetDocumentTextMethod;
    if ((getGetDocumentTextMethod = EventsGrpc.getGetDocumentTextMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetDocumentTextMethod = EventsGrpc.getGetDocumentTextMethod) == null) {
          EventsGrpc.getGetDocumentTextMethod = getGetDocumentTextMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetDocumentText"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetDocumentText"))
              .build();
        }
      }
    }
    return getGetDocumentTextMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse> getGetLabelIndicesInfoMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetLabelIndicesInfo",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse> getGetLabelIndicesInfoMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse> getGetLabelIndicesInfoMethod;
    if ((getGetLabelIndicesInfoMethod = EventsGrpc.getGetLabelIndicesInfoMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetLabelIndicesInfoMethod = EventsGrpc.getGetLabelIndicesInfoMethod) == null) {
          EventsGrpc.getGetLabelIndicesInfoMethod = getGetLabelIndicesInfoMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetLabelIndicesInfo"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetLabelIndicesInfo"))
              .build();
        }
      }
    }
    return getGetLabelIndicesInfoMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse> getAddLabelsMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AddLabels",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse> getAddLabelsMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse> getAddLabelsMethod;
    if ((getAddLabelsMethod = EventsGrpc.getAddLabelsMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getAddLabelsMethod = EventsGrpc.getAddLabelsMethod) == null) {
          EventsGrpc.getAddLabelsMethod = getAddLabelsMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AddLabels"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("AddLabels"))
              .build();
        }
      }
    }
    return getAddLabelsMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse> getGetLabelsMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetLabels",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse> getGetLabelsMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse> getGetLabelsMethod;
    if ((getGetLabelsMethod = EventsGrpc.getGetLabelsMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetLabelsMethod = EventsGrpc.getGetLabelsMethod) == null) {
          EventsGrpc.getGetLabelsMethod = getGetLabelsMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetLabels"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetLabels"))
              .build();
        }
      }
    }
    return getGetLabelsMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse> getGetAllBinaryDataNamesMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetAllBinaryDataNames",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse> getGetAllBinaryDataNamesMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse> getGetAllBinaryDataNamesMethod;
    if ((getGetAllBinaryDataNamesMethod = EventsGrpc.getGetAllBinaryDataNamesMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetAllBinaryDataNamesMethod = EventsGrpc.getGetAllBinaryDataNamesMethod) == null) {
          EventsGrpc.getGetAllBinaryDataNamesMethod = getGetAllBinaryDataNamesMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetAllBinaryDataNames"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetAllBinaryDataNames"))
              .build();
        }
      }
    }
    return getGetAllBinaryDataNamesMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse> getAddBinaryDataMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AddBinaryData",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse> getAddBinaryDataMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse> getAddBinaryDataMethod;
    if ((getAddBinaryDataMethod = EventsGrpc.getAddBinaryDataMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getAddBinaryDataMethod = EventsGrpc.getAddBinaryDataMethod) == null) {
          EventsGrpc.getAddBinaryDataMethod = getAddBinaryDataMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AddBinaryData"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("AddBinaryData"))
              .build();
        }
      }
    }
    return getAddBinaryDataMethod;
  }

  private static volatile io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse> getGetBinaryDataMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetBinaryData",
      requestType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest.class,
      responseType = edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest,
      edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse> getGetBinaryDataMethod() {
    io.grpc.MethodDescriptor<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse> getGetBinaryDataMethod;
    if ((getGetBinaryDataMethod = EventsGrpc.getGetBinaryDataMethod) == null) {
      synchronized (EventsGrpc.class) {
        if ((getGetBinaryDataMethod = EventsGrpc.getGetBinaryDataMethod) == null) {
          EventsGrpc.getGetBinaryDataMethod = getGetBinaryDataMethod =
              io.grpc.MethodDescriptor.<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest, edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetBinaryData"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse.getDefaultInstance()))
              .setSchemaDescriptor(new EventsMethodDescriptorSupplier("GetBinaryData"))
              .build();
        }
      }
    }
    return getGetBinaryDataMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static EventsStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<EventsStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<EventsStub>() {
        @java.lang.Override
        public EventsStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new EventsStub(channel, callOptions);
        }
      };
    return EventsStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static EventsBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<EventsBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<EventsBlockingStub>() {
        @java.lang.Override
        public EventsBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new EventsBlockingStub(channel, callOptions);
        }
      };
    return EventsBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static EventsFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<EventsFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<EventsFutureStub>() {
        @java.lang.Override
        public EventsFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new EventsFutureStub(channel, callOptions);
        }
      };
    return EventsFutureStub.newStub(factory, channel);
  }

  /**
   * <pre>
   * The events service, which stores Events (the top level discrete processing
   * objects a mapping of strings to Documents and strings to strings metadata),
   * Documents (a text string and a mapping of strings to LabelIndices), and
   * LabelIndices (collections of objects which mark locations in text having
   * some meaning).
   * </pre>
   */
  public static abstract class EventsImplBase implements io.grpc.BindableService {

    /**
     */
    public void getEventsInstanceId(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetEventsInstanceIdMethod(), responseObserver);
    }

    /**
     * <pre>
     * Acquires a lease for an event, which will prevent this service
     * from deleting the event while the lease is still valid. Can be used to
     * either create new events or return existing events.
     * </pre>
     */
    public void openEvent(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getOpenEventMethod(), responseObserver);
    }

    /**
     * <pre>
     * Cedes a lease for an event, allowing this service to delete the
     * event if no active leases remain.
     * </pre>
     */
    public void closeEvent(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getCloseEventMethod(), responseObserver);
    }

    /**
     * <pre>
     * Endpoint to get all metadata associated with an event.
     * </pre>
     */
    public void getAllMetadata(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetAllMetadataMethod(), responseObserver);
    }

    /**
     * <pre>
     * Adds a new metadata entry to an event.
     * </pre>
     */
    public void addMetadata(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAddMetadataMethod(), responseObserver);
    }

    /**
     * <pre>
     * Adds a new document to an event.
     * </pre>
     */
    public void addDocument(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAddDocumentMethod(), responseObserver);
    }

    /**
     * <pre>
     * Returns the names keys of all documents that are stored on an event.
     * </pre>
     */
    public void getAllDocumentNames(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetAllDocumentNamesMethod(), responseObserver);
    }

    /**
     * <pre>
     * Returns the text of a document.
     * </pre>
     */
    public void getDocumentText(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetDocumentTextMethod(), responseObserver);
    }

    /**
     * <pre>
     * Returns the names keys of all label indices that are stored on a document.
     * </pre>
     */
    public void getLabelIndicesInfo(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetLabelIndicesInfoMethod(), responseObserver);
    }

    /**
     * <pre>
     * Adds a single label index to the document.
     * </pre>
     */
    public void addLabels(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAddLabelsMethod(), responseObserver);
    }

    /**
     * <pre>
     * Gets all of the labels for a single label index.
     * </pre>
     */
    public void getLabels(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetLabelsMethod(), responseObserver);
    }

    /**
     */
    public void getAllBinaryDataNames(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetAllBinaryDataNamesMethod(), responseObserver);
    }

    /**
     */
    public void addBinaryData(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAddBinaryDataMethod(), responseObserver);
    }

    /**
     */
    public void getBinaryData(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetBinaryDataMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getGetEventsInstanceIdMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse>(
                  this, METHODID_GET_EVENTS_INSTANCE_ID)))
          .addMethod(
            getOpenEventMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse>(
                  this, METHODID_OPEN_EVENT)))
          .addMethod(
            getCloseEventMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse>(
                  this, METHODID_CLOSE_EVENT)))
          .addMethod(
            getGetAllMetadataMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse>(
                  this, METHODID_GET_ALL_METADATA)))
          .addMethod(
            getAddMetadataMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse>(
                  this, METHODID_ADD_METADATA)))
          .addMethod(
            getAddDocumentMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse>(
                  this, METHODID_ADD_DOCUMENT)))
          .addMethod(
            getGetAllDocumentNamesMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse>(
                  this, METHODID_GET_ALL_DOCUMENT_NAMES)))
          .addMethod(
            getGetDocumentTextMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse>(
                  this, METHODID_GET_DOCUMENT_TEXT)))
          .addMethod(
            getGetLabelIndicesInfoMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse>(
                  this, METHODID_GET_LABEL_INDICES_INFO)))
          .addMethod(
            getAddLabelsMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse>(
                  this, METHODID_ADD_LABELS)))
          .addMethod(
            getGetLabelsMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse>(
                  this, METHODID_GET_LABELS)))
          .addMethod(
            getGetAllBinaryDataNamesMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse>(
                  this, METHODID_GET_ALL_BINARY_DATA_NAMES)))
          .addMethod(
            getAddBinaryDataMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse>(
                  this, METHODID_ADD_BINARY_DATA)))
          .addMethod(
            getGetBinaryDataMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest,
                edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse>(
                  this, METHODID_GET_BINARY_DATA)))
          .build();
    }
  }

  /**
   * <pre>
   * The events service, which stores Events (the top level discrete processing
   * objects a mapping of strings to Documents and strings to strings metadata),
   * Documents (a text string and a mapping of strings to LabelIndices), and
   * LabelIndices (collections of objects which mark locations in text having
   * some meaning).
   * </pre>
   */
  public static final class EventsStub extends io.grpc.stub.AbstractAsyncStub<EventsStub> {
    private EventsStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected EventsStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new EventsStub(channel, callOptions);
    }

    /**
     */
    public void getEventsInstanceId(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetEventsInstanceIdMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Acquires a lease for an event, which will prevent this service
     * from deleting the event while the lease is still valid. Can be used to
     * either create new events or return existing events.
     * </pre>
     */
    public void openEvent(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getOpenEventMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Cedes a lease for an event, allowing this service to delete the
     * event if no active leases remain.
     * </pre>
     */
    public void closeEvent(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getCloseEventMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Endpoint to get all metadata associated with an event.
     * </pre>
     */
    public void getAllMetadata(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetAllMetadataMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Adds a new metadata entry to an event.
     * </pre>
     */
    public void addMetadata(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAddMetadataMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Adds a new document to an event.
     * </pre>
     */
    public void addDocument(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAddDocumentMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Returns the names keys of all documents that are stored on an event.
     * </pre>
     */
    public void getAllDocumentNames(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetAllDocumentNamesMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Returns the text of a document.
     * </pre>
     */
    public void getDocumentText(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetDocumentTextMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Returns the names keys of all label indices that are stored on a document.
     * </pre>
     */
    public void getLabelIndicesInfo(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetLabelIndicesInfoMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Adds a single label index to the document.
     * </pre>
     */
    public void addLabels(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAddLabelsMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Gets all of the labels for a single label index.
     * </pre>
     */
    public void getLabels(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetLabelsMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void getAllBinaryDataNames(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetAllBinaryDataNamesMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void addBinaryData(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAddBinaryDataMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void getBinaryData(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest request,
        io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetBinaryDataMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * <pre>
   * The events service, which stores Events (the top level discrete processing
   * objects a mapping of strings to Documents and strings to strings metadata),
   * Documents (a text string and a mapping of strings to LabelIndices), and
   * LabelIndices (collections of objects which mark locations in text having
   * some meaning).
   * </pre>
   */
  public static final class EventsBlockingStub extends io.grpc.stub.AbstractBlockingStub<EventsBlockingStub> {
    private EventsBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected EventsBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new EventsBlockingStub(channel, callOptions);
    }

    /**
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse getEventsInstanceId(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetEventsInstanceIdMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Acquires a lease for an event, which will prevent this service
     * from deleting the event while the lease is still valid. Can be used to
     * either create new events or return existing events.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse openEvent(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getOpenEventMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Cedes a lease for an event, allowing this service to delete the
     * event if no active leases remain.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse closeEvent(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getCloseEventMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Endpoint to get all metadata associated with an event.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse getAllMetadata(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetAllMetadataMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Adds a new metadata entry to an event.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse addMetadata(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAddMetadataMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Adds a new document to an event.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse addDocument(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAddDocumentMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Returns the names keys of all documents that are stored on an event.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse getAllDocumentNames(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetAllDocumentNamesMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Returns the text of a document.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse getDocumentText(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetDocumentTextMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Returns the names keys of all label indices that are stored on a document.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse getLabelIndicesInfo(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetLabelIndicesInfoMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Adds a single label index to the document.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse addLabels(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAddLabelsMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Gets all of the labels for a single label index.
     * </pre>
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse getLabels(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetLabelsMethod(), getCallOptions(), request);
    }

    /**
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse getAllBinaryDataNames(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetAllBinaryDataNamesMethod(), getCallOptions(), request);
    }

    /**
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse addBinaryData(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAddBinaryDataMethod(), getCallOptions(), request);
    }

    /**
     */
    public edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse getBinaryData(edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetBinaryDataMethod(), getCallOptions(), request);
    }
  }

  /**
   * <pre>
   * The events service, which stores Events (the top level discrete processing
   * objects a mapping of strings to Documents and strings to strings metadata),
   * Documents (a text string and a mapping of strings to LabelIndices), and
   * LabelIndices (collections of objects which mark locations in text having
   * some meaning).
   * </pre>
   */
  public static final class EventsFutureStub extends io.grpc.stub.AbstractFutureStub<EventsFutureStub> {
    private EventsFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected EventsFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new EventsFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse> getEventsInstanceId(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetEventsInstanceIdMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Acquires a lease for an event, which will prevent this service
     * from deleting the event while the lease is still valid. Can be used to
     * either create new events or return existing events.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse> openEvent(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getOpenEventMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Cedes a lease for an event, allowing this service to delete the
     * event if no active leases remain.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse> closeEvent(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getCloseEventMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Endpoint to get all metadata associated with an event.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse> getAllMetadata(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetAllMetadataMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Adds a new metadata entry to an event.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse> addMetadata(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAddMetadataMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Adds a new document to an event.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse> addDocument(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAddDocumentMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Returns the names keys of all documents that are stored on an event.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse> getAllDocumentNames(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetAllDocumentNamesMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Returns the text of a document.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse> getDocumentText(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetDocumentTextMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Returns the names keys of all label indices that are stored on a document.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse> getLabelIndicesInfo(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetLabelIndicesInfoMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Adds a single label index to the document.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse> addLabels(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAddLabelsMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Gets all of the labels for a single label index.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse> getLabels(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetLabelsMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse> getAllBinaryDataNames(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetAllBinaryDataNamesMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse> addBinaryData(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAddBinaryDataMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse> getBinaryData(
        edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetBinaryDataMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_GET_EVENTS_INSTANCE_ID = 0;
  private static final int METHODID_OPEN_EVENT = 1;
  private static final int METHODID_CLOSE_EVENT = 2;
  private static final int METHODID_GET_ALL_METADATA = 3;
  private static final int METHODID_ADD_METADATA = 4;
  private static final int METHODID_ADD_DOCUMENT = 5;
  private static final int METHODID_GET_ALL_DOCUMENT_NAMES = 6;
  private static final int METHODID_GET_DOCUMENT_TEXT = 7;
  private static final int METHODID_GET_LABEL_INDICES_INFO = 8;
  private static final int METHODID_ADD_LABELS = 9;
  private static final int METHODID_GET_LABELS = 10;
  private static final int METHODID_GET_ALL_BINARY_DATA_NAMES = 11;
  private static final int METHODID_ADD_BINARY_DATA = 12;
  private static final int METHODID_GET_BINARY_DATA = 13;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final EventsImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(EventsImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_GET_EVENTS_INSTANCE_ID:
          serviceImpl.getEventsInstanceId((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetEventsInstanceIdResponse>) responseObserver);
          break;
        case METHODID_OPEN_EVENT:
          serviceImpl.openEvent((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.OpenEventResponse>) responseObserver);
          break;
        case METHODID_CLOSE_EVENT:
          serviceImpl.closeEvent((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.CloseEventResponse>) responseObserver);
          break;
        case METHODID_GET_ALL_METADATA:
          serviceImpl.getAllMetadata((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllMetadataResponse>) responseObserver);
          break;
        case METHODID_ADD_METADATA:
          serviceImpl.addMetadata((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddMetadataResponse>) responseObserver);
          break;
        case METHODID_ADD_DOCUMENT:
          serviceImpl.addDocument((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddDocumentResponse>) responseObserver);
          break;
        case METHODID_GET_ALL_DOCUMENT_NAMES:
          serviceImpl.getAllDocumentNames((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllDocumentNamesResponse>) responseObserver);
          break;
        case METHODID_GET_DOCUMENT_TEXT:
          serviceImpl.getDocumentText((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetDocumentTextResponse>) responseObserver);
          break;
        case METHODID_GET_LABEL_INDICES_INFO:
          serviceImpl.getLabelIndicesInfo((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelIndicesInfoResponse>) responseObserver);
          break;
        case METHODID_ADD_LABELS:
          serviceImpl.addLabels((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddLabelsResponse>) responseObserver);
          break;
        case METHODID_GET_LABELS:
          serviceImpl.getLabels((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetLabelsResponse>) responseObserver);
          break;
        case METHODID_GET_ALL_BINARY_DATA_NAMES:
          serviceImpl.getAllBinaryDataNames((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetAllBinaryDataNamesResponse>) responseObserver);
          break;
        case METHODID_ADD_BINARY_DATA:
          serviceImpl.addBinaryData((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.AddBinaryDataResponse>) responseObserver);
          break;
        case METHODID_GET_BINARY_DATA:
          serviceImpl.getBinaryData((edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataRequest) request,
              (io.grpc.stub.StreamObserver<edu.umn.nlpie.mtap.api.v1.EventsOuterClass.GetBinaryDataResponse>) responseObserver);
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

  private static abstract class EventsBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    EventsBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return edu.umn.nlpie.mtap.api.v1.EventsOuterClass.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Events");
    }
  }

  private static final class EventsFileDescriptorSupplier
      extends EventsBaseDescriptorSupplier {
    EventsFileDescriptorSupplier() {}
  }

  private static final class EventsMethodDescriptorSupplier
      extends EventsBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    EventsMethodDescriptorSupplier(String methodName) {
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
      synchronized (EventsGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new EventsFileDescriptorSupplier())
              .addMethod(getGetEventsInstanceIdMethod())
              .addMethod(getOpenEventMethod())
              .addMethod(getCloseEventMethod())
              .addMethod(getGetAllMetadataMethod())
              .addMethod(getAddMetadataMethod())
              .addMethod(getAddDocumentMethod())
              .addMethod(getGetAllDocumentNamesMethod())
              .addMethod(getGetDocumentTextMethod())
              .addMethod(getGetLabelIndicesInfoMethod())
              .addMethod(getAddLabelsMethod())
              .addMethod(getGetLabelsMethod())
              .addMethod(getGetAllBinaryDataNamesMethod())
              .addMethod(getAddBinaryDataMethod())
              .addMethod(getGetBinaryDataMethod())
              .build();
        }
      }
    }
    return result;
  }
}
