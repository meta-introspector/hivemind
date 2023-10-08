# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p2pd.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\np2pd.proto\x12\x11p2pclient.p2pd.pb\"\xc9\x05\n\x07Request\x12-\n\x04type\x18\x01 \x02(\x0e\x32\x1f.p2pclient.p2pd.pb.Request.Type\x12\x32\n\x07\x63onnect\x18\x02 \x01(\x0b\x32!.p2pclient.p2pd.pb.ConnectRequest\x12\x38\n\nstreamOpen\x18\x03 \x01(\x0b\x32$.p2pclient.p2pd.pb.StreamOpenRequest\x12>\n\rstreamHandler\x18\x04 \x01(\x0b\x32\'.p2pclient.p2pd.pb.StreamHandlerRequest\x12J\n\x13removeStreamHandler\x18\t \x01(\x0b\x32-.p2pclient.p2pd.pb.RemoveStreamHandlerRequest\x12*\n\x03\x64ht\x18\x05 \x01(\x0b\x32\x1d.p2pclient.p2pd.pb.DHTRequest\x12:\n\x0b\x63onnManager\x18\x06 \x01(\x0b\x32%.p2pclient.p2pd.pb.ConnManagerRequest\x12\x38\n\ndisconnect\x18\x07 \x01(\x0b\x32$.p2pclient.p2pd.pb.DisconnectRequest\x12,\n\x06pubsub\x18\x08 \x01(\x0b\x32\x1c.p2pclient.p2pd.pb.PSRequest\"\xc4\x01\n\x04Type\x12\x0c\n\x08IDENTIFY\x10\x00\x12\x0b\n\x07\x43ONNECT\x10\x01\x12\x0f\n\x0bSTREAM_OPEN\x10\x02\x12\x12\n\x0eSTREAM_HANDLER\x10\x03\x12\x19\n\x15REMOVE_STREAM_HANDLER\x10\n\x12\x07\n\x03\x44HT\x10\x04\x12\x0e\n\nLIST_PEERS\x10\x05\x12\x0f\n\x0b\x43ONNMANAGER\x10\x06\x12\x0e\n\nDISCONNECT\x10\x07\x12\n\n\x06PUBSUB\x10\x08\x12\x1b\n\x17PERSISTENT_CONN_UPGRADE\x10\t\"\xf8\x02\n\x08Response\x12.\n\x04type\x18\x01 \x02(\x0e\x32 .p2pclient.p2pd.pb.Response.Type\x12/\n\x05\x65rror\x18\x02 \x01(\x0b\x32 .p2pclient.p2pd.pb.ErrorResponse\x12\x31\n\nstreamInfo\x18\x03 \x01(\x0b\x32\x1d.p2pclient.p2pd.pb.StreamInfo\x12\x35\n\x08identify\x18\x04 \x01(\x0b\x32#.p2pclient.p2pd.pb.IdentifyResponse\x12+\n\x03\x64ht\x18\x05 \x01(\x0b\x32\x1e.p2pclient.p2pd.pb.DHTResponse\x12*\n\x05peers\x18\x06 \x03(\x0b\x32\x1b.p2pclient.p2pd.pb.PeerInfo\x12-\n\x06pubsub\x18\x07 \x01(\x0b\x32\x1d.p2pclient.p2pd.pb.PSResponse\"\x19\n\x04Type\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"\xf0\x02\n\x1bPersistentConnectionRequest\x12\x0e\n\x06\x63\x61llId\x18\x01 \x02(\x0c\x12\x44\n\x0f\x61\x64\x64UnaryHandler\x18\x02 \x01(\x0b\x32).p2pclient.p2pd.pb.AddUnaryHandlerRequestH\x00\x12J\n\x12removeUnaryHandler\x18\x06 \x01(\x0b\x32,.p2pclient.p2pd.pb.RemoveUnaryHandlerRequestH\x00\x12\x38\n\tcallUnary\x18\x03 \x01(\x0b\x32#.p2pclient.p2pd.pb.CallUnaryRequestH\x00\x12=\n\runaryResponse\x18\x04 \x01(\x0b\x32$.p2pclient.p2pd.pb.CallUnaryResponseH\x00\x12+\n\x06\x63\x61ncel\x18\x05 \x01(\x0b\x32\x19.p2pclient.p2pd.pb.CancelH\x00\x42\t\n\x07message\"\xa0\x02\n\x1cPersistentConnectionResponse\x12\x0e\n\x06\x63\x61llId\x18\x01 \x02(\x0c\x12\x41\n\x11\x63\x61llUnaryResponse\x18\x02 \x01(\x0b\x32$.p2pclient.p2pd.pb.CallUnaryResponseH\x00\x12>\n\x0frequestHandling\x18\x03 \x01(\x0b\x32#.p2pclient.p2pd.pb.CallUnaryRequestH\x00\x12\x35\n\x0b\x64\x61\x65monError\x18\x04 \x01(\x0b\x32\x1e.p2pclient.p2pd.pb.DaemonErrorH\x00\x12+\n\x06\x63\x61ncel\x18\x05 \x01(\x0b\x32\x19.p2pclient.p2pd.pb.CancelH\x00\x42\t\n\x07message\"-\n\x10IdentifyResponse\x12\n\n\x02id\x18\x01 \x02(\x0c\x12\r\n\x05\x61\x64\x64rs\x18\x02 \x03(\x0c\">\n\x0e\x43onnectRequest\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\x12\r\n\x05\x61\x64\x64rs\x18\x02 \x03(\x0c\x12\x0f\n\x07timeout\x18\x03 \x01(\x03\"A\n\x11StreamOpenRequest\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\x12\r\n\x05proto\x18\x02 \x03(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x03\"E\n\x14StreamHandlerRequest\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x02(\x0c\x12\r\n\x05proto\x18\x02 \x03(\t\x12\x10\n\x08\x62\x61lanced\x18\x03 \x02(\x08\"9\n\x1aRemoveStreamHandlerRequest\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x02(\x0c\x12\r\n\x05proto\x18\x02 \x03(\t\"\x1c\n\rErrorResponse\x12\x0b\n\x03msg\x18\x01 \x02(\t\"7\n\nStreamInfo\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x02(\x0c\x12\r\n\x05proto\x18\x03 \x02(\t\"\xcb\x02\n\nDHTRequest\x12\x30\n\x04type\x18\x01 \x02(\x0e\x32\".p2pclient.p2pd.pb.DHTRequest.Type\x12\x0c\n\x04peer\x18\x02 \x01(\x0c\x12\x0b\n\x03\x63id\x18\x03 \x01(\x0c\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\r\n\x05value\x18\x05 \x01(\x0c\x12\r\n\x05\x63ount\x18\x06 \x01(\x05\x12\x0f\n\x07timeout\x18\x07 \x01(\x03\"\xb3\x01\n\x04Type\x12\r\n\tFIND_PEER\x10\x00\x12 \n\x1c\x46IND_PEERS_CONNECTED_TO_PEER\x10\x01\x12\x12\n\x0e\x46IND_PROVIDERS\x10\x02\x12\x15\n\x11GET_CLOSEST_PEERS\x10\x03\x12\x12\n\x0eGET_PUBLIC_KEY\x10\x04\x12\r\n\tGET_VALUE\x10\x05\x12\x10\n\x0cSEARCH_VALUE\x10\x06\x12\r\n\tPUT_VALUE\x10\x07\x12\x0b\n\x07PROVIDE\x10\x08\"\xa1\x01\n\x0b\x44HTResponse\x12\x31\n\x04type\x18\x01 \x02(\x0e\x32#.p2pclient.p2pd.pb.DHTResponse.Type\x12)\n\x04peer\x18\x02 \x01(\x0b\x32\x1b.p2pclient.p2pd.pb.PeerInfo\x12\r\n\x05value\x18\x03 \x01(\x0c\"%\n\x04Type\x12\t\n\x05\x42\x45GIN\x10\x00\x12\t\n\x05VALUE\x10\x01\x12\x07\n\x03\x45ND\x10\x02\"%\n\x08PeerInfo\x12\n\n\x02id\x18\x01 \x02(\x0c\x12\r\n\x05\x61\x64\x64rs\x18\x02 \x03(\x0c\"\xa9\x01\n\x12\x43onnManagerRequest\x12\x38\n\x04type\x18\x01 \x02(\x0e\x32*.p2pclient.p2pd.pb.ConnManagerRequest.Type\x12\x0c\n\x04peer\x18\x02 \x01(\x0c\x12\x0b\n\x03tag\x18\x03 \x01(\t\x12\x0e\n\x06weight\x18\x04 \x01(\x03\".\n\x04Type\x12\x0c\n\x08TAG_PEER\x10\x00\x12\x0e\n\nUNTAG_PEER\x10\x01\x12\x08\n\x04TRIM\x10\x02\"!\n\x11\x44isconnectRequest\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\"\x9d\x01\n\tPSRequest\x12/\n\x04type\x18\x01 \x02(\x0e\x32!.p2pclient.p2pd.pb.PSRequest.Type\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"B\n\x04Type\x12\x0e\n\nGET_TOPICS\x10\x00\x12\x0e\n\nLIST_PEERS\x10\x01\x12\x0b\n\x07PUBLISH\x10\x02\x12\r\n\tSUBSCRIBE\x10\x03\"h\n\tPSMessage\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\r\n\x05seqno\x18\x03 \x01(\x0c\x12\x10\n\x08topicIDs\x18\x04 \x03(\t\x12\x11\n\tsignature\x18\x05 \x01(\x0c\x12\x0b\n\x03key\x18\x06 \x01(\x0c\"-\n\nPSResponse\x12\x0e\n\x06topics\x18\x01 \x03(\t\x12\x0f\n\x07peerIDs\x18\x02 \x03(\x0c\"=\n\x10\x43\x61llUnaryRequest\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\x12\r\n\x05proto\x18\x02 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\x0c\"B\n\x11\x43\x61llUnaryResponse\x12\x12\n\x08response\x18\x01 \x01(\x0cH\x00\x12\x0f\n\x05\x65rror\x18\x02 \x01(\x0cH\x00\x42\x08\n\x06result\"9\n\x16\x41\x64\x64UnaryHandlerRequest\x12\r\n\x05proto\x18\x01 \x02(\t\x12\x10\n\x08\x62\x61lanced\x18\x02 \x02(\x08\"*\n\x19RemoveUnaryHandlerRequest\x12\r\n\x05proto\x18\x01 \x02(\t\"\x1e\n\x0b\x44\x61\x65monError\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x08\n\x06\x43\x61ncel\"\x1b\n\x08RPCError\x12\x0f\n\x07message\x18\x01 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'p2pd_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=34
  _globals['_REQUEST']._serialized_end=747
  _globals['_REQUEST_TYPE']._serialized_start=551
  _globals['_REQUEST_TYPE']._serialized_end=747
  _globals['_RESPONSE']._serialized_start=750
  _globals['_RESPONSE']._serialized_end=1126
  _globals['_RESPONSE_TYPE']._serialized_start=1101
  _globals['_RESPONSE_TYPE']._serialized_end=1126
  _globals['_PERSISTENTCONNECTIONREQUEST']._serialized_start=1129
  _globals['_PERSISTENTCONNECTIONREQUEST']._serialized_end=1497
  _globals['_PERSISTENTCONNECTIONRESPONSE']._serialized_start=1500
  _globals['_PERSISTENTCONNECTIONRESPONSE']._serialized_end=1788
  _globals['_IDENTIFYRESPONSE']._serialized_start=1790
  _globals['_IDENTIFYRESPONSE']._serialized_end=1835
  _globals['_CONNECTREQUEST']._serialized_start=1837
  _globals['_CONNECTREQUEST']._serialized_end=1899
  _globals['_STREAMOPENREQUEST']._serialized_start=1901
  _globals['_STREAMOPENREQUEST']._serialized_end=1966
  _globals['_STREAMHANDLERREQUEST']._serialized_start=1968
  _globals['_STREAMHANDLERREQUEST']._serialized_end=2037
  _globals['_REMOVESTREAMHANDLERREQUEST']._serialized_start=2039
  _globals['_REMOVESTREAMHANDLERREQUEST']._serialized_end=2096
  _globals['_ERRORRESPONSE']._serialized_start=2098
  _globals['_ERRORRESPONSE']._serialized_end=2126
  _globals['_STREAMINFO']._serialized_start=2128
  _globals['_STREAMINFO']._serialized_end=2183
  _globals['_DHTREQUEST']._serialized_start=2186
  _globals['_DHTREQUEST']._serialized_end=2517
  _globals['_DHTREQUEST_TYPE']._serialized_start=2338
  _globals['_DHTREQUEST_TYPE']._serialized_end=2517
  _globals['_DHTRESPONSE']._serialized_start=2520
  _globals['_DHTRESPONSE']._serialized_end=2681
  _globals['_DHTRESPONSE_TYPE']._serialized_start=2644
  _globals['_DHTRESPONSE_TYPE']._serialized_end=2681
  _globals['_PEERINFO']._serialized_start=2683
  _globals['_PEERINFO']._serialized_end=2720
  _globals['_CONNMANAGERREQUEST']._serialized_start=2723
  _globals['_CONNMANAGERREQUEST']._serialized_end=2892
  _globals['_CONNMANAGERREQUEST_TYPE']._serialized_start=2846
  _globals['_CONNMANAGERREQUEST_TYPE']._serialized_end=2892
  _globals['_DISCONNECTREQUEST']._serialized_start=2894
  _globals['_DISCONNECTREQUEST']._serialized_end=2927
  _globals['_PSREQUEST']._serialized_start=2930
  _globals['_PSREQUEST']._serialized_end=3087
  _globals['_PSREQUEST_TYPE']._serialized_start=3021
  _globals['_PSREQUEST_TYPE']._serialized_end=3087
  _globals['_PSMESSAGE']._serialized_start=3089
  _globals['_PSMESSAGE']._serialized_end=3193
  _globals['_PSRESPONSE']._serialized_start=3195
  _globals['_PSRESPONSE']._serialized_end=3240
  _globals['_CALLUNARYREQUEST']._serialized_start=3242
  _globals['_CALLUNARYREQUEST']._serialized_end=3303
  _globals['_CALLUNARYRESPONSE']._serialized_start=3305
  _globals['_CALLUNARYRESPONSE']._serialized_end=3371
  _globals['_ADDUNARYHANDLERREQUEST']._serialized_start=3373
  _globals['_ADDUNARYHANDLERREQUEST']._serialized_end=3430
  _globals['_REMOVEUNARYHANDLERREQUEST']._serialized_start=3432
  _globals['_REMOVEUNARYHANDLERREQUEST']._serialized_end=3474
  _globals['_DAEMONERROR']._serialized_start=3476
  _globals['_DAEMONERROR']._serialized_end=3506
  _globals['_CANCEL']._serialized_start=3508
  _globals['_CANCEL']._serialized_end=3516
  _globals['_RPCERROR']._serialized_start=3518
  _globals['_RPCERROR']._serialized_end=3545
# @@protoc_insertion_point(module_scope)