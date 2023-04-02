// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v3.12.4
// source: image.proto

package image

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Image struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name       string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Dockerfile string `protobuf:"bytes,2,opt,name=dockerfile,proto3" json:"dockerfile,omitempty"`
	Tag        string `protobuf:"bytes,3,opt,name=tag,proto3" json:"tag,omitempty"`
}

func (x *Image) Reset() {
	*x = Image{}
	if protoimpl.UnsafeEnabled {
		mi := &file_image_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Image) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Image) ProtoMessage() {}

func (x *Image) ProtoReflect() protoreflect.Message {
	mi := &file_image_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Image.ProtoReflect.Descriptor instead.
func (*Image) Descriptor() ([]byte, []int) {
	return file_image_proto_rawDescGZIP(), []int{0}
}

func (x *Image) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *Image) GetDockerfile() string {
	if x != nil {
		return x.Dockerfile
	}
	return ""
}

func (x *Image) GetTag() string {
	if x != nil {
		return x.Tag
	}
	return ""
}

type Error struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Type  string `protobuf:"bytes,1,opt,name=type,proto3" json:"type,omitempty"`
	Error string `protobuf:"bytes,2,opt,name=error,proto3" json:"error,omitempty"`
}

func (x *Error) Reset() {
	*x = Error{}
	if protoimpl.UnsafeEnabled {
		mi := &file_image_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Error) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Error) ProtoMessage() {}

func (x *Error) ProtoReflect() protoreflect.Message {
	mi := &file_image_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Error.ProtoReflect.Descriptor instead.
func (*Error) Descriptor() ([]byte, []int) {
	return file_image_proto_rawDescGZIP(), []int{1}
}

func (x *Error) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

func (x *Error) GetError() string {
	if x != nil {
		return x.Error
	}
	return ""
}

type Success struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Type string `protobuf:"bytes,1,opt,name=type,proto3" json:"type,omitempty"`
	Msg  string `protobuf:"bytes,2,opt,name=msg,proto3" json:"msg,omitempty"`
}

func (x *Success) Reset() {
	*x = Success{}
	if protoimpl.UnsafeEnabled {
		mi := &file_image_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Success) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Success) ProtoMessage() {}

func (x *Success) ProtoReflect() protoreflect.Message {
	mi := &file_image_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Success.ProtoReflect.Descriptor instead.
func (*Success) Descriptor() ([]byte, []int) {
	return file_image_proto_rawDescGZIP(), []int{2}
}

func (x *Success) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

func (x *Success) GetMsg() string {
	if x != nil {
		return x.Msg
	}
	return ""
}

type ImageBuildSuccess struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Tag  string `protobuf:"bytes,2,opt,name=tag,proto3" json:"tag,omitempty"`
}

func (x *ImageBuildSuccess) Reset() {
	*x = ImageBuildSuccess{}
	if protoimpl.UnsafeEnabled {
		mi := &file_image_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ImageBuildSuccess) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ImageBuildSuccess) ProtoMessage() {}

func (x *ImageBuildSuccess) ProtoReflect() protoreflect.Message {
	mi := &file_image_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ImageBuildSuccess.ProtoReflect.Descriptor instead.
func (*ImageBuildSuccess) Descriptor() ([]byte, []int) {
	return file_image_proto_rawDescGZIP(), []int{3}
}

func (x *ImageBuildSuccess) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *ImageBuildSuccess) GetTag() string {
	if x != nil {
		return x.Tag
	}
	return ""
}

type ImageBuildResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Responses:
	//
	//	*ImageBuildResponse_Success
	//	*ImageBuildResponse_Error
	Responses isImageBuildResponse_Responses `protobuf_oneof:"responses"`
}

func (x *ImageBuildResponse) Reset() {
	*x = ImageBuildResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_image_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ImageBuildResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ImageBuildResponse) ProtoMessage() {}

func (x *ImageBuildResponse) ProtoReflect() protoreflect.Message {
	mi := &file_image_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ImageBuildResponse.ProtoReflect.Descriptor instead.
func (*ImageBuildResponse) Descriptor() ([]byte, []int) {
	return file_image_proto_rawDescGZIP(), []int{4}
}

func (m *ImageBuildResponse) GetResponses() isImageBuildResponse_Responses {
	if m != nil {
		return m.Responses
	}
	return nil
}

func (x *ImageBuildResponse) GetSuccess() *ImageBuildSuccess {
	if x, ok := x.GetResponses().(*ImageBuildResponse_Success); ok {
		return x.Success
	}
	return nil
}

func (x *ImageBuildResponse) GetError() *Error {
	if x, ok := x.GetResponses().(*ImageBuildResponse_Error); ok {
		return x.Error
	}
	return nil
}

type isImageBuildResponse_Responses interface {
	isImageBuildResponse_Responses()
}

type ImageBuildResponse_Success struct {
	Success *ImageBuildSuccess `protobuf:"bytes,1,opt,name=success,proto3,oneof"`
}

type ImageBuildResponse_Error struct {
	Error *Error `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

func (*ImageBuildResponse_Success) isImageBuildResponse_Responses() {}

func (*ImageBuildResponse_Error) isImageBuildResponse_Responses() {}

type ImageRegistryDetails struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name       string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Tag        string `protobuf:"bytes,2,opt,name=tag,proto3" json:"tag,omitempty"`
	Hub        string `protobuf:"bytes,3,opt,name=hub,proto3" json:"hub,omitempty"`
	Credential string `protobuf:"bytes,4,opt,name=credential,proto3" json:"credential,omitempty"`
}

func (x *ImageRegistryDetails) Reset() {
	*x = ImageRegistryDetails{}
	if protoimpl.UnsafeEnabled {
		mi := &file_image_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ImageRegistryDetails) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ImageRegistryDetails) ProtoMessage() {}

func (x *ImageRegistryDetails) ProtoReflect() protoreflect.Message {
	mi := &file_image_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ImageRegistryDetails.ProtoReflect.Descriptor instead.
func (*ImageRegistryDetails) Descriptor() ([]byte, []int) {
	return file_image_proto_rawDescGZIP(), []int{5}
}

func (x *ImageRegistryDetails) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *ImageRegistryDetails) GetTag() string {
	if x != nil {
		return x.Tag
	}
	return ""
}

func (x *ImageRegistryDetails) GetHub() string {
	if x != nil {
		return x.Hub
	}
	return ""
}

func (x *ImageRegistryDetails) GetCredential() string {
	if x != nil {
		return x.Credential
	}
	return ""
}

type GenericResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Responses:
	//
	//	*GenericResponse_Success
	//	*GenericResponse_Error
	Responses isGenericResponse_Responses `protobuf_oneof:"responses"`
}

func (x *GenericResponse) Reset() {
	*x = GenericResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_image_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GenericResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GenericResponse) ProtoMessage() {}

func (x *GenericResponse) ProtoReflect() protoreflect.Message {
	mi := &file_image_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GenericResponse.ProtoReflect.Descriptor instead.
func (*GenericResponse) Descriptor() ([]byte, []int) {
	return file_image_proto_rawDescGZIP(), []int{6}
}

func (m *GenericResponse) GetResponses() isGenericResponse_Responses {
	if m != nil {
		return m.Responses
	}
	return nil
}

func (x *GenericResponse) GetSuccess() *Success {
	if x, ok := x.GetResponses().(*GenericResponse_Success); ok {
		return x.Success
	}
	return nil
}

func (x *GenericResponse) GetError() *Error {
	if x, ok := x.GetResponses().(*GenericResponse_Error); ok {
		return x.Error
	}
	return nil
}

type isGenericResponse_Responses interface {
	isGenericResponse_Responses()
}

type GenericResponse_Success struct {
	Success *Success `protobuf:"bytes,1,opt,name=success,proto3,oneof"`
}

type GenericResponse_Error struct {
	Error *Error `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

func (*GenericResponse_Success) isGenericResponse_Responses() {}

func (*GenericResponse_Error) isGenericResponse_Responses() {}

var File_image_proto protoreflect.FileDescriptor

var file_image_proto_rawDesc = []byte{
	0x0a, 0x0b, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x05, 0x69,
	0x6d, 0x61, 0x67, 0x65, 0x22, 0x4d, 0x0a, 0x05, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x12, 0x12, 0x0a,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x12, 0x1e, 0x0a, 0x0a, 0x64, 0x6f, 0x63, 0x6b, 0x65, 0x72, 0x66, 0x69, 0x6c, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x64, 0x6f, 0x63, 0x6b, 0x65, 0x72, 0x66, 0x69, 0x6c,
	0x65, 0x12, 0x10, 0x0a, 0x03, 0x74, 0x61, 0x67, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03,
	0x74, 0x61, 0x67, 0x22, 0x31, 0x0a, 0x05, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x12, 0x12, 0x0a, 0x04,
	0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65,
	0x12, 0x14, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x2f, 0x0a, 0x07, 0x53, 0x75, 0x63, 0x63, 0x65, 0x73,
	0x73, 0x12, 0x12, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x04, 0x74, 0x79, 0x70, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x6d, 0x73, 0x67, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x03, 0x6d, 0x73, 0x67, 0x22, 0x39, 0x0a, 0x11, 0x49, 0x6d, 0x61, 0x67, 0x65,
	0x42, 0x75, 0x69, 0x6c, 0x64, 0x53, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x12, 0x12, 0x0a, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65,
	0x12, 0x10, 0x0a, 0x03, 0x74, 0x61, 0x67, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x74,
	0x61, 0x67, 0x22, 0x7d, 0x0a, 0x12, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x42, 0x75, 0x69, 0x6c, 0x64,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x34, 0x0a, 0x07, 0x73, 0x75, 0x63, 0x63,
	0x65, 0x73, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x18, 0x2e, 0x69, 0x6d, 0x61, 0x67,
	0x65, 0x2e, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x42, 0x75, 0x69, 0x6c, 0x64, 0x53, 0x75, 0x63, 0x63,
	0x65, 0x73, 0x73, 0x48, 0x00, 0x52, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x12, 0x24,
	0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0c, 0x2e,
	0x69, 0x6d, 0x61, 0x67, 0x65, 0x2e, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65,
	0x72, 0x72, 0x6f, 0x72, 0x42, 0x0b, 0x0a, 0x09, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x73, 0x22, 0x6e, 0x0a, 0x14, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x52, 0x65, 0x67, 0x69, 0x73, 0x74,
	0x72, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x10, 0x0a,
	0x03, 0x74, 0x61, 0x67, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x74, 0x61, 0x67, 0x12,
	0x10, 0x0a, 0x03, 0x68, 0x75, 0x62, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x68, 0x75,
	0x62, 0x12, 0x1e, 0x0a, 0x0a, 0x63, 0x72, 0x65, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x61, 0x6c, 0x18,
	0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x72, 0x65, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x61,
	0x6c, 0x22, 0x70, 0x0a, 0x0f, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x69, 0x63, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x2a, 0x0a, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0e, 0x2e, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x2e, 0x53, 0x75,
	0x63, 0x63, 0x65, 0x73, 0x73, 0x48, 0x00, 0x52, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73,
	0x12, 0x24, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x0c, 0x2e, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x2e, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52,
	0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x42, 0x0b, 0x0a, 0x09, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x73, 0x32, 0x85, 0x01, 0x0a, 0x06, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x73, 0x12, 0x37,
	0x0a, 0x0a, 0x62, 0x75, 0x69, 0x6c, 0x64, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x12, 0x0c, 0x2e, 0x69,
	0x6d, 0x61, 0x67, 0x65, 0x2e, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x1a, 0x19, 0x2e, 0x69, 0x6d, 0x61,
	0x67, 0x65, 0x2e, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x42, 0x75, 0x69, 0x6c, 0x64, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x42, 0x0a, 0x09, 0x70, 0x75, 0x73, 0x68, 0x49,
	0x6d, 0x61, 0x67, 0x65, 0x12, 0x1b, 0x2e, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x2e, 0x49, 0x6d, 0x61,
	0x67, 0x65, 0x52, 0x65, 0x67, 0x69, 0x73, 0x74, 0x72, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c,
	0x73, 0x1a, 0x16, 0x2e, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x2e, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x69,
	0x63, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x42, 0x09, 0x5a, 0x07, 0x2e,
	0x2f, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_image_proto_rawDescOnce sync.Once
	file_image_proto_rawDescData = file_image_proto_rawDesc
)

func file_image_proto_rawDescGZIP() []byte {
	file_image_proto_rawDescOnce.Do(func() {
		file_image_proto_rawDescData = protoimpl.X.CompressGZIP(file_image_proto_rawDescData)
	})
	return file_image_proto_rawDescData
}

var file_image_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_image_proto_goTypes = []interface{}{
	(*Image)(nil),                // 0: image.Image
	(*Error)(nil),                // 1: image.Error
	(*Success)(nil),              // 2: image.Success
	(*ImageBuildSuccess)(nil),    // 3: image.ImageBuildSuccess
	(*ImageBuildResponse)(nil),   // 4: image.ImageBuildResponse
	(*ImageRegistryDetails)(nil), // 5: image.ImageRegistryDetails
	(*GenericResponse)(nil),      // 6: image.GenericResponse
}
var file_image_proto_depIdxs = []int32{
	3, // 0: image.ImageBuildResponse.success:type_name -> image.ImageBuildSuccess
	1, // 1: image.ImageBuildResponse.error:type_name -> image.Error
	2, // 2: image.GenericResponse.success:type_name -> image.Success
	1, // 3: image.GenericResponse.error:type_name -> image.Error
	0, // 4: image.Images.buildImage:input_type -> image.Image
	5, // 5: image.Images.pushImage:input_type -> image.ImageRegistryDetails
	4, // 6: image.Images.buildImage:output_type -> image.ImageBuildResponse
	6, // 7: image.Images.pushImage:output_type -> image.GenericResponse
	6, // [6:8] is the sub-list for method output_type
	4, // [4:6] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_image_proto_init() }
func file_image_proto_init() {
	if File_image_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_image_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Image); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_image_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Error); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_image_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Success); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_image_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ImageBuildSuccess); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_image_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ImageBuildResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_image_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ImageRegistryDetails); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_image_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GenericResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_image_proto_msgTypes[4].OneofWrappers = []interface{}{
		(*ImageBuildResponse_Success)(nil),
		(*ImageBuildResponse_Error)(nil),
	}
	file_image_proto_msgTypes[6].OneofWrappers = []interface{}{
		(*GenericResponse_Success)(nil),
		(*GenericResponse_Error)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_image_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_image_proto_goTypes,
		DependencyIndexes: file_image_proto_depIdxs,
		MessageInfos:      file_image_proto_msgTypes,
	}.Build()
	File_image_proto = out.File
	file_image_proto_rawDesc = nil
	file_image_proto_goTypes = nil
	file_image_proto_depIdxs = nil
}