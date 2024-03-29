/**
 * @fileoverview gRPC-Web generated client stub for environment
 * @enhanceable
 * @public
 */

// Code generated by protoc-gen-grpc-web. DO NOT EDIT.
// versions:
// 	protoc-gen-grpc-web v1.4.2
// 	protoc              v3.12.4
// source: environment.proto


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.environment = require('./environment_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.environment.environmentClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname.replace(/\/+$/, '');

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.environment.environmentPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname.replace(/\/+$/, '');

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.environment.EnvironmentRequest,
 *   !proto.environment.EnvCreationResponse>}
 */
const methodDescriptor_environment_createEnvironment = new grpc.web.MethodDescriptor(
  '/environment.environment/createEnvironment',
  grpc.web.MethodType.SERVER_STREAMING,
  proto.environment.EnvironmentRequest,
  proto.environment.EnvCreationResponse,
  /**
   * @param {!proto.environment.EnvironmentRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.environment.EnvCreationResponse.deserializeBinary
);


/**
 * @param {!proto.environment.EnvironmentRequest} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.environment.EnvCreationResponse>}
 *     The XHR Node Readable Stream
 */
proto.environment.environmentClient.prototype.createEnvironment =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/environment.environment/createEnvironment',
      request,
      metadata || {},
      methodDescriptor_environment_createEnvironment);
};


/**
 * @param {!proto.environment.EnvironmentRequest} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.environment.EnvCreationResponse>}
 *     The XHR Node Readable Stream
 */
proto.environment.environmentPromiseClient.prototype.createEnvironment =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/environment.environment/createEnvironment',
      request,
      metadata || {},
      methodDescriptor_environment_createEnvironment);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.environment.EnvModReq,
 *   !proto.environment.Response>}
 */
const methodDescriptor_environment_deleteEnvironment = new grpc.web.MethodDescriptor(
  '/environment.environment/deleteEnvironment',
  grpc.web.MethodType.UNARY,
  proto.environment.EnvModReq,
  proto.environment.Response,
  /**
   * @param {!proto.environment.EnvModReq} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.environment.Response.deserializeBinary
);


/**
 * @param {!proto.environment.EnvModReq} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.environment.Response)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.environment.Response>|undefined}
 *     The XHR Node Readable Stream
 */
proto.environment.environmentClient.prototype.deleteEnvironment =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/environment.environment/deleteEnvironment',
      request,
      metadata || {},
      methodDescriptor_environment_deleteEnvironment,
      callback);
};


/**
 * @param {!proto.environment.EnvModReq} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.environment.Response>}
 *     Promise that resolves to the response
 */
proto.environment.environmentPromiseClient.prototype.deleteEnvironment =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/environment.environment/deleteEnvironment',
      request,
      metadata || {},
      methodDescriptor_environment_deleteEnvironment);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.environment.EnvModReq,
 *   !proto.environment.Response>}
 */
const methodDescriptor_environment_stopEnvironment = new grpc.web.MethodDescriptor(
  '/environment.environment/stopEnvironment',
  grpc.web.MethodType.UNARY,
  proto.environment.EnvModReq,
  proto.environment.Response,
  /**
   * @param {!proto.environment.EnvModReq} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.environment.Response.deserializeBinary
);


/**
 * @param {!proto.environment.EnvModReq} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.environment.Response)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.environment.Response>|undefined}
 *     The XHR Node Readable Stream
 */
proto.environment.environmentClient.prototype.stopEnvironment =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/environment.environment/stopEnvironment',
      request,
      metadata || {},
      methodDescriptor_environment_stopEnvironment,
      callback);
};


/**
 * @param {!proto.environment.EnvModReq} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.environment.Response>}
 *     Promise that resolves to the response
 */
proto.environment.environmentPromiseClient.prototype.stopEnvironment =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/environment.environment/stopEnvironment',
      request,
      metadata || {},
      methodDescriptor_environment_stopEnvironment);
};


module.exports = proto.environment;
