/**
 * @fileoverview gRPC-Web generated client stub for execution
 * @enhanceable
 * @public
 */

// Code generated by protoc-gen-grpc-web. DO NOT EDIT.
// versions:
// 	protoc-gen-grpc-web v1.4.2
// 	protoc              v3.12.4
// source: execute.proto


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.execution = require('./execute_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.execution.ExecuteClient =
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
proto.execution.ExecutePromiseClient =
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
 *   !proto.execution.ExecuteRequest,
 *   !proto.execution.ExecutionResponse>}
 */
const methodDescriptor_Execute_executeCommand = new grpc.web.MethodDescriptor(
  '/execution.Execute/executeCommand',
  grpc.web.MethodType.UNARY,
  proto.execution.ExecuteRequest,
  proto.execution.ExecutionResponse,
  /**
   * @param {!proto.execution.ExecuteRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.execution.ExecutionResponse.deserializeBinary
);


/**
 * @param {!proto.execution.ExecuteRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.execution.ExecutionResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.execution.ExecutionResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.execution.ExecuteClient.prototype.executeCommand =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/execution.Execute/executeCommand',
      request,
      metadata || {},
      methodDescriptor_Execute_executeCommand,
      callback);
};


/**
 * @param {!proto.execution.ExecuteRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.execution.ExecutionResponse>}
 *     Promise that resolves to the response
 */
proto.execution.ExecutePromiseClient.prototype.executeCommand =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/execution.Execute/executeCommand',
      request,
      metadata || {},
      methodDescriptor_Execute_executeCommand);
};


module.exports = proto.execution;
