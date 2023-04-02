// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v3.12.4
// source: execute.proto

package execution

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

type ExecuteRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ContainerName string `protobuf:"bytes,1,opt,name=container_name,json=containerName,proto3" json:"container_name,omitempty"`
	Command       string `protobuf:"bytes,2,opt,name=command,proto3" json:"command,omitempty"`
}

func (x *ExecuteRequest) Reset() {
	*x = ExecuteRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_execute_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ExecuteRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ExecuteRequest) ProtoMessage() {}

func (x *ExecuteRequest) ProtoReflect() protoreflect.Message {
	mi := &file_execute_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ExecuteRequest.ProtoReflect.Descriptor instead.
func (*ExecuteRequest) Descriptor() ([]byte, []int) {
	return file_execute_proto_rawDescGZIP(), []int{0}
}

func (x *ExecuteRequest) GetContainerName() string {
	if x != nil {
		return x.ContainerName
	}
	return ""
}

func (x *ExecuteRequest) GetCommand() string {
	if x != nil {
		return x.Command
	}
	return ""
}

type ExecutionSuccess struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Result string `protobuf:"bytes,1,opt,name=result,proto3" json:"result,omitempty"`
}

func (x *ExecutionSuccess) Reset() {
	*x = ExecutionSuccess{}
	if protoimpl.UnsafeEnabled {
		mi := &file_execute_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ExecutionSuccess) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ExecutionSuccess) ProtoMessage() {}

func (x *ExecutionSuccess) ProtoReflect() protoreflect.Message {
	mi := &file_execute_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ExecutionSuccess.ProtoReflect.Descriptor instead.
func (*ExecutionSuccess) Descriptor() ([]byte, []int) {
	return file_execute_proto_rawDescGZIP(), []int{1}
}

func (x *ExecutionSuccess) GetResult() string {
	if x != nil {
		return x.Result
	}
	return ""
}

type Error struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error string `protobuf:"bytes,1,opt,name=error,proto3" json:"error,omitempty"`
}

func (x *Error) Reset() {
	*x = Error{}
	if protoimpl.UnsafeEnabled {
		mi := &file_execute_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Error) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Error) ProtoMessage() {}

func (x *Error) ProtoReflect() protoreflect.Message {
	mi := &file_execute_proto_msgTypes[2]
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
	return file_execute_proto_rawDescGZIP(), []int{2}
}

func (x *Error) GetError() string {
	if x != nil {
		return x.Error
	}
	return ""
}

type ExecutionResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Responses:
	//
	//	*ExecutionResponse_Success
	//	*ExecutionResponse_Error
	Responses isExecutionResponse_Responses `protobuf_oneof:"responses"`
}

func (x *ExecutionResponse) Reset() {
	*x = ExecutionResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_execute_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ExecutionResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ExecutionResponse) ProtoMessage() {}

func (x *ExecutionResponse) ProtoReflect() protoreflect.Message {
	mi := &file_execute_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ExecutionResponse.ProtoReflect.Descriptor instead.
func (*ExecutionResponse) Descriptor() ([]byte, []int) {
	return file_execute_proto_rawDescGZIP(), []int{3}
}

func (m *ExecutionResponse) GetResponses() isExecutionResponse_Responses {
	if m != nil {
		return m.Responses
	}
	return nil
}

func (x *ExecutionResponse) GetSuccess() *ExecutionSuccess {
	if x, ok := x.GetResponses().(*ExecutionResponse_Success); ok {
		return x.Success
	}
	return nil
}

func (x *ExecutionResponse) GetError() *Error {
	if x, ok := x.GetResponses().(*ExecutionResponse_Error); ok {
		return x.Error
	}
	return nil
}

type isExecutionResponse_Responses interface {
	isExecutionResponse_Responses()
}

type ExecutionResponse_Success struct {
	Success *ExecutionSuccess `protobuf:"bytes,1,opt,name=success,proto3,oneof"`
}

type ExecutionResponse_Error struct {
	Error *Error `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

func (*ExecutionResponse_Success) isExecutionResponse_Responses() {}

func (*ExecutionResponse_Error) isExecutionResponse_Responses() {}

var File_execute_proto protoreflect.FileDescriptor

var file_execute_proto_rawDesc = []byte{
	0x0a, 0x0d, 0x65, 0x78, 0x65, 0x63, 0x75, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x09, 0x65, 0x78, 0x65, 0x63, 0x75, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x51, 0x0a, 0x0e, 0x45, 0x78,
	0x65, 0x63, 0x75, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x25, 0x0a, 0x0e,
	0x63, 0x6f, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x0d, 0x63, 0x6f, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x4e,
	0x61, 0x6d, 0x65, 0x12, 0x18, 0x0a, 0x07, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x22, 0x2a, 0x0a,
	0x10, 0x45, 0x78, 0x65, 0x63, 0x75, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x75, 0x63, 0x63, 0x65, 0x73,
	0x73, 0x12, 0x16, 0x0a, 0x06, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x06, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x22, 0x1d, 0x0a, 0x05, 0x45, 0x72, 0x72,
	0x6f, 0x72, 0x12, 0x14, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x83, 0x01, 0x0a, 0x11, 0x45, 0x78, 0x65,
	0x63, 0x75, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x37,
	0x0a, 0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x1b, 0x2e, 0x65, 0x78, 0x65, 0x63, 0x75, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x45, 0x78, 0x65, 0x63,
	0x75, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x48, 0x00, 0x52, 0x07,
	0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x12, 0x28, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x65, 0x78, 0x65, 0x63, 0x75, 0x74, 0x69,
	0x6f, 0x6e, 0x2e, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f,
	0x72, 0x42, 0x0b, 0x0a, 0x09, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x73, 0x32, 0x56,
	0x0a, 0x07, 0x45, 0x78, 0x65, 0x63, 0x75, 0x74, 0x65, 0x12, 0x4b, 0x0a, 0x0e, 0x65, 0x78, 0x65,
	0x63, 0x75, 0x74, 0x65, 0x43, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x12, 0x19, 0x2e, 0x65, 0x78,
	0x65, 0x63, 0x75, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x45, 0x78, 0x65, 0x63, 0x75, 0x74, 0x65, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1c, 0x2e, 0x65, 0x78, 0x65, 0x63, 0x75, 0x74, 0x69,
	0x6f, 0x6e, 0x2e, 0x45, 0x78, 0x65, 0x63, 0x75, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x42, 0x0d, 0x5a, 0x0b, 0x2e, 0x2f, 0x65, 0x78, 0x65, 0x63,
	0x75, 0x74, 0x69, 0x6f, 0x6e, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_execute_proto_rawDescOnce sync.Once
	file_execute_proto_rawDescData = file_execute_proto_rawDesc
)

func file_execute_proto_rawDescGZIP() []byte {
	file_execute_proto_rawDescOnce.Do(func() {
		file_execute_proto_rawDescData = protoimpl.X.CompressGZIP(file_execute_proto_rawDescData)
	})
	return file_execute_proto_rawDescData
}

var file_execute_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_execute_proto_goTypes = []interface{}{
	(*ExecuteRequest)(nil),    // 0: execution.ExecuteRequest
	(*ExecutionSuccess)(nil),  // 1: execution.ExecutionSuccess
	(*Error)(nil),             // 2: execution.Error
	(*ExecutionResponse)(nil), // 3: execution.ExecutionResponse
}
var file_execute_proto_depIdxs = []int32{
	1, // 0: execution.ExecutionResponse.success:type_name -> execution.ExecutionSuccess
	2, // 1: execution.ExecutionResponse.error:type_name -> execution.Error
	0, // 2: execution.Execute.executeCommand:input_type -> execution.ExecuteRequest
	3, // 3: execution.Execute.executeCommand:output_type -> execution.ExecutionResponse
	3, // [3:4] is the sub-list for method output_type
	2, // [2:3] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_execute_proto_init() }
func file_execute_proto_init() {
	if File_execute_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_execute_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ExecuteRequest); i {
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
		file_execute_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ExecutionSuccess); i {
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
		file_execute_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
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
		file_execute_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ExecutionResponse); i {
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
	file_execute_proto_msgTypes[3].OneofWrappers = []interface{}{
		(*ExecutionResponse_Success)(nil),
		(*ExecutionResponse_Error)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_execute_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_execute_proto_goTypes,
		DependencyIndexes: file_execute_proto_depIdxs,
		MessageInfos:      file_execute_proto_msgTypes,
	}.Build()
	File_execute_proto = out.File
	file_execute_proto_rawDesc = nil
	file_execute_proto_goTypes = nil
	file_execute_proto_depIdxs = nil
}