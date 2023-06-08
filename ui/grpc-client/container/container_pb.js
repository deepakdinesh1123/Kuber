// source: container.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.container.Container', null, global);
goog.exportSymbol('proto.container.ContainerCreated', null, global);
goog.exportSymbol('proto.container.ContainerCreationError', null, global);
goog.exportSymbol('proto.container.ContainerCreationResponse', null, global);
goog.exportSymbol('proto.container.ContainerCreationResponse.ResponseCase', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.container.Container = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.container.Container, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.container.Container.displayName = 'proto.container.Container';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.container.ContainerCreated = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.container.ContainerCreated, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.container.ContainerCreated.displayName = 'proto.container.ContainerCreated';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.container.ContainerCreationError = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.container.ContainerCreationError, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.container.ContainerCreationError.displayName = 'proto.container.ContainerCreationError';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.container.ContainerCreationResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.container.ContainerCreationResponse.oneofGroups_);
};
goog.inherits(proto.container.ContainerCreationResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.container.ContainerCreationResponse.displayName = 'proto.container.ContainerCreationResponse';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.container.Container.prototype.toObject = function(opt_includeInstance) {
  return proto.container.Container.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.container.Container} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.Container.toObject = function(includeInstance, msg) {
  var f, obj = {
    name: jspb.Message.getFieldWithDefault(msg, 1, ""),
    image: jspb.Message.getFieldWithDefault(msg, 2, ""),
    network: jspb.Message.getFieldWithDefault(msg, 3, ""),
    config: jspb.Message.getFieldWithDefault(msg, 4, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.container.Container}
 */
proto.container.Container.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.container.Container;
  return proto.container.Container.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.container.Container} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.container.Container}
 */
proto.container.Container.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setImage(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setNetwork(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setConfig(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.container.Container.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.container.Container.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.container.Container} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.Container.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getImage();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getNetwork();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getConfig();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
};


/**
 * optional string name = 1;
 * @return {string}
 */
proto.container.Container.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.container.Container} returns this
 */
proto.container.Container.prototype.setName = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string image = 2;
 * @return {string}
 */
proto.container.Container.prototype.getImage = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.container.Container} returns this
 */
proto.container.Container.prototype.setImage = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional string network = 3;
 * @return {string}
 */
proto.container.Container.prototype.getNetwork = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.container.Container} returns this
 */
proto.container.Container.prototype.setNetwork = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional string config = 4;
 * @return {string}
 */
proto.container.Container.prototype.getConfig = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/**
 * @param {string} value
 * @return {!proto.container.Container} returns this
 */
proto.container.Container.prototype.setConfig = function(value) {
  return jspb.Message.setProto3StringField(this, 4, value);
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.container.ContainerCreated.prototype.toObject = function(opt_includeInstance) {
  return proto.container.ContainerCreated.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.container.ContainerCreated} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.ContainerCreated.toObject = function(includeInstance, msg) {
  var f, obj = {
    name: jspb.Message.getFieldWithDefault(msg, 1, ""),
    logs: jspb.Message.getFieldWithDefault(msg, 3, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.container.ContainerCreated}
 */
proto.container.ContainerCreated.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.container.ContainerCreated;
  return proto.container.ContainerCreated.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.container.ContainerCreated} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.container.ContainerCreated}
 */
proto.container.ContainerCreated.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setLogs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.container.ContainerCreated.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.container.ContainerCreated.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.container.ContainerCreated} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.ContainerCreated.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getLogs();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
};


/**
 * optional string name = 1;
 * @return {string}
 */
proto.container.ContainerCreated.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.container.ContainerCreated} returns this
 */
proto.container.ContainerCreated.prototype.setName = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string logs = 3;
 * @return {string}
 */
proto.container.ContainerCreated.prototype.getLogs = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.container.ContainerCreated} returns this
 */
proto.container.ContainerCreated.prototype.setLogs = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.container.ContainerCreationError.prototype.toObject = function(opt_includeInstance) {
  return proto.container.ContainerCreationError.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.container.ContainerCreationError} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.ContainerCreationError.toObject = function(includeInstance, msg) {
  var f, obj = {
    error: jspb.Message.getFieldWithDefault(msg, 1, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.container.ContainerCreationError}
 */
proto.container.ContainerCreationError.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.container.ContainerCreationError;
  return proto.container.ContainerCreationError.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.container.ContainerCreationError} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.container.ContainerCreationError}
 */
proto.container.ContainerCreationError.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setError(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.container.ContainerCreationError.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.container.ContainerCreationError.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.container.ContainerCreationError} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.ContainerCreationError.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getError();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
};


/**
 * optional string error = 1;
 * @return {string}
 */
proto.container.ContainerCreationError.prototype.getError = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.container.ContainerCreationError} returns this
 */
proto.container.ContainerCreationError.prototype.setError = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};



/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.container.ContainerCreationResponse.oneofGroups_ = [[1,2]];

/**
 * @enum {number}
 */
proto.container.ContainerCreationResponse.ResponseCase = {
  RESPONSE_NOT_SET: 0,
  CONTAINER_CREATED: 1,
  CONTAINER_ERROR: 2
};

/**
 * @return {proto.container.ContainerCreationResponse.ResponseCase}
 */
proto.container.ContainerCreationResponse.prototype.getResponseCase = function() {
  return /** @type {proto.container.ContainerCreationResponse.ResponseCase} */(jspb.Message.computeOneofCase(this, proto.container.ContainerCreationResponse.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.container.ContainerCreationResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.container.ContainerCreationResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.container.ContainerCreationResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.ContainerCreationResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    containerCreated: (f = msg.getContainerCreated()) && proto.container.ContainerCreated.toObject(includeInstance, f),
    containerError: (f = msg.getContainerError()) && proto.container.ContainerCreationError.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.container.ContainerCreationResponse}
 */
proto.container.ContainerCreationResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.container.ContainerCreationResponse;
  return proto.container.ContainerCreationResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.container.ContainerCreationResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.container.ContainerCreationResponse}
 */
proto.container.ContainerCreationResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.container.ContainerCreated;
      reader.readMessage(value,proto.container.ContainerCreated.deserializeBinaryFromReader);
      msg.setContainerCreated(value);
      break;
    case 2:
      var value = new proto.container.ContainerCreationError;
      reader.readMessage(value,proto.container.ContainerCreationError.deserializeBinaryFromReader);
      msg.setContainerError(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.container.ContainerCreationResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.container.ContainerCreationResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.container.ContainerCreationResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.container.ContainerCreationResponse.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getContainerCreated();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.container.ContainerCreated.serializeBinaryToWriter
    );
  }
  f = message.getContainerError();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      proto.container.ContainerCreationError.serializeBinaryToWriter
    );
  }
};


/**
 * optional ContainerCreated container_created = 1;
 * @return {?proto.container.ContainerCreated}
 */
proto.container.ContainerCreationResponse.prototype.getContainerCreated = function() {
  return /** @type{?proto.container.ContainerCreated} */ (
    jspb.Message.getWrapperField(this, proto.container.ContainerCreated, 1));
};


/**
 * @param {?proto.container.ContainerCreated|undefined} value
 * @return {!proto.container.ContainerCreationResponse} returns this
*/
proto.container.ContainerCreationResponse.prototype.setContainerCreated = function(value) {
  return jspb.Message.setOneofWrapperField(this, 1, proto.container.ContainerCreationResponse.oneofGroups_[0], value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.container.ContainerCreationResponse} returns this
 */
proto.container.ContainerCreationResponse.prototype.clearContainerCreated = function() {
  return this.setContainerCreated(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.container.ContainerCreationResponse.prototype.hasContainerCreated = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional ContainerCreationError container_error = 2;
 * @return {?proto.container.ContainerCreationError}
 */
proto.container.ContainerCreationResponse.prototype.getContainerError = function() {
  return /** @type{?proto.container.ContainerCreationError} */ (
    jspb.Message.getWrapperField(this, proto.container.ContainerCreationError, 2));
};


/**
 * @param {?proto.container.ContainerCreationError|undefined} value
 * @return {!proto.container.ContainerCreationResponse} returns this
*/
proto.container.ContainerCreationResponse.prototype.setContainerError = function(value) {
  return jspb.Message.setOneofWrapperField(this, 2, proto.container.ContainerCreationResponse.oneofGroups_[0], value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.container.ContainerCreationResponse} returns this
 */
proto.container.ContainerCreationResponse.prototype.clearContainerError = function() {
  return this.setContainerError(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.container.ContainerCreationResponse.prototype.hasContainerError = function() {
  return jspb.Message.getField(this, 2) != null;
};


goog.object.extend(exports, proto.container);
