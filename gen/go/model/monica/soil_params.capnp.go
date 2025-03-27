// Code generated by capnpc-go. DO NOT EDIT.

package monica

import (
	capnp "capnproto.org/go/capnp/v3"
	text "capnproto.org/go/capnp/v3/encoding/text"
	schemas "capnproto.org/go/capnp/v3/schemas"
	math "math"
)

type SoilCharacteristicData capnp.Struct

// SoilCharacteristicData_TypeID is the unique identifier for the type SoilCharacteristicData.
const SoilCharacteristicData_TypeID = 0xfc682227304e2281

func NewSoilCharacteristicData(s *capnp.Segment) (SoilCharacteristicData, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1})
	return SoilCharacteristicData(st), err
}

func NewRootSoilCharacteristicData(s *capnp.Segment) (SoilCharacteristicData, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1})
	return SoilCharacteristicData(st), err
}

func ReadRootSoilCharacteristicData(msg *capnp.Message) (SoilCharacteristicData, error) {
	root, err := msg.Root()
	return SoilCharacteristicData(root.Struct()), err
}

func (s SoilCharacteristicData) String() string {
	str, _ := text.Marshal(0xfc682227304e2281, capnp.Struct(s))
	return str
}

func (s SoilCharacteristicData) EncodeAsPtr(seg *capnp.Segment) capnp.Ptr {
	return capnp.Struct(s).EncodeAsPtr(seg)
}

func (SoilCharacteristicData) DecodeFromPtr(p capnp.Ptr) SoilCharacteristicData {
	return SoilCharacteristicData(capnp.Struct{}.DecodeFromPtr(p))
}

func (s SoilCharacteristicData) ToPtr() capnp.Ptr {
	return capnp.Struct(s).ToPtr()
}
func (s SoilCharacteristicData) IsValid() bool {
	return capnp.Struct(s).IsValid()
}

func (s SoilCharacteristicData) Message() *capnp.Message {
	return capnp.Struct(s).Message()
}

func (s SoilCharacteristicData) Segment() *capnp.Segment {
	return capnp.Struct(s).Segment()
}
func (s SoilCharacteristicData) List() (SoilCharacteristicData_Data_List, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return SoilCharacteristicData_Data_List(p.List()), err
}

func (s SoilCharacteristicData) HasList() bool {
	return capnp.Struct(s).HasPtr(0)
}

func (s SoilCharacteristicData) SetList(v SoilCharacteristicData_Data_List) error {
	return capnp.Struct(s).SetPtr(0, v.ToPtr())
}

// NewList sets the list field to a newly
// allocated SoilCharacteristicData_Data_List, preferring placement in s's segment.
func (s SoilCharacteristicData) NewList(n int32) (SoilCharacteristicData_Data_List, error) {
	l, err := NewSoilCharacteristicData_Data_List(capnp.Struct(s).Segment(), n)
	if err != nil {
		return SoilCharacteristicData_Data_List{}, err
	}
	err = capnp.Struct(s).SetPtr(0, l.ToPtr())
	return l, err
}

// SoilCharacteristicData_List is a list of SoilCharacteristicData.
type SoilCharacteristicData_List = capnp.StructList[SoilCharacteristicData]

// NewSoilCharacteristicData creates a new list of SoilCharacteristicData.
func NewSoilCharacteristicData_List(s *capnp.Segment, sz int32) (SoilCharacteristicData_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1}, sz)
	return capnp.StructList[SoilCharacteristicData](l), err
}

// SoilCharacteristicData_Future is a wrapper for a SoilCharacteristicData promised by a client call.
type SoilCharacteristicData_Future struct{ *capnp.Future }

func (f SoilCharacteristicData_Future) Struct() (SoilCharacteristicData, error) {
	p, err := f.Future.Ptr()
	return SoilCharacteristicData(p.Struct()), err
}

type SoilCharacteristicData_Data capnp.Struct

// SoilCharacteristicData_Data_TypeID is the unique identifier for the type SoilCharacteristicData_Data.
const SoilCharacteristicData_Data_TypeID = 0xeafaab57e025db63

func NewSoilCharacteristicData_Data(s *capnp.Segment) (SoilCharacteristicData_Data, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	return SoilCharacteristicData_Data(st), err
}

func NewRootSoilCharacteristicData_Data(s *capnp.Segment) (SoilCharacteristicData_Data, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	return SoilCharacteristicData_Data(st), err
}

func ReadRootSoilCharacteristicData_Data(msg *capnp.Message) (SoilCharacteristicData_Data, error) {
	root, err := msg.Root()
	return SoilCharacteristicData_Data(root.Struct()), err
}

func (s SoilCharacteristicData_Data) String() string {
	str, _ := text.Marshal(0xeafaab57e025db63, capnp.Struct(s))
	return str
}

func (s SoilCharacteristicData_Data) EncodeAsPtr(seg *capnp.Segment) capnp.Ptr {
	return capnp.Struct(s).EncodeAsPtr(seg)
}

func (SoilCharacteristicData_Data) DecodeFromPtr(p capnp.Ptr) SoilCharacteristicData_Data {
	return SoilCharacteristicData_Data(capnp.Struct{}.DecodeFromPtr(p))
}

func (s SoilCharacteristicData_Data) ToPtr() capnp.Ptr {
	return capnp.Struct(s).ToPtr()
}
func (s SoilCharacteristicData_Data) IsValid() bool {
	return capnp.Struct(s).IsValid()
}

func (s SoilCharacteristicData_Data) Message() *capnp.Message {
	return capnp.Struct(s).Message()
}

func (s SoilCharacteristicData_Data) Segment() *capnp.Segment {
	return capnp.Struct(s).Segment()
}
func (s SoilCharacteristicData_Data) SoilType() (string, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return p.Text(), err
}

func (s SoilCharacteristicData_Data) HasSoilType() bool {
	return capnp.Struct(s).HasPtr(0)
}

func (s SoilCharacteristicData_Data) SoilTypeBytes() ([]byte, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return p.TextBytes(), err
}

func (s SoilCharacteristicData_Data) SetSoilType(v string) error {
	return capnp.Struct(s).SetText(0, v)
}

func (s SoilCharacteristicData_Data) SoilRawDensity() int16 {
	return int16(capnp.Struct(s).Uint16(0))
}

func (s SoilCharacteristicData_Data) SetSoilRawDensity(v int16) {
	capnp.Struct(s).SetUint16(0, uint16(v))
}

func (s SoilCharacteristicData_Data) AirCapacity() uint8 {
	return capnp.Struct(s).Uint8(2)
}

func (s SoilCharacteristicData_Data) SetAirCapacity(v uint8) {
	capnp.Struct(s).SetUint8(2, v)
}

func (s SoilCharacteristicData_Data) FieldCapacity() uint8 {
	return capnp.Struct(s).Uint8(3)
}

func (s SoilCharacteristicData_Data) SetFieldCapacity(v uint8) {
	capnp.Struct(s).SetUint8(3, v)
}

func (s SoilCharacteristicData_Data) NFieldCapacity() uint8 {
	return capnp.Struct(s).Uint8(4)
}

func (s SoilCharacteristicData_Data) SetNFieldCapacity(v uint8) {
	capnp.Struct(s).SetUint8(4, v)
}

// SoilCharacteristicData_Data_List is a list of SoilCharacteristicData_Data.
type SoilCharacteristicData_Data_List = capnp.StructList[SoilCharacteristicData_Data]

// NewSoilCharacteristicData_Data creates a new list of SoilCharacteristicData_Data.
func NewSoilCharacteristicData_Data_List(s *capnp.Segment, sz int32) (SoilCharacteristicData_Data_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1}, sz)
	return capnp.StructList[SoilCharacteristicData_Data](l), err
}

// SoilCharacteristicData_Data_Future is a wrapper for a SoilCharacteristicData_Data promised by a client call.
type SoilCharacteristicData_Data_Future struct{ *capnp.Future }

func (f SoilCharacteristicData_Data_Future) Struct() (SoilCharacteristicData_Data, error) {
	p, err := f.Future.Ptr()
	return SoilCharacteristicData_Data(p.Struct()), err
}

type SoilCharacteristicModifier capnp.Struct

// SoilCharacteristicModifier_TypeID is the unique identifier for the type SoilCharacteristicModifier.
const SoilCharacteristicModifier_TypeID = 0xe4eb0a9bb0e5bb53

func NewSoilCharacteristicModifier(s *capnp.Segment) (SoilCharacteristicModifier, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1})
	return SoilCharacteristicModifier(st), err
}

func NewRootSoilCharacteristicModifier(s *capnp.Segment) (SoilCharacteristicModifier, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1})
	return SoilCharacteristicModifier(st), err
}

func ReadRootSoilCharacteristicModifier(msg *capnp.Message) (SoilCharacteristicModifier, error) {
	root, err := msg.Root()
	return SoilCharacteristicModifier(root.Struct()), err
}

func (s SoilCharacteristicModifier) String() string {
	str, _ := text.Marshal(0xe4eb0a9bb0e5bb53, capnp.Struct(s))
	return str
}

func (s SoilCharacteristicModifier) EncodeAsPtr(seg *capnp.Segment) capnp.Ptr {
	return capnp.Struct(s).EncodeAsPtr(seg)
}

func (SoilCharacteristicModifier) DecodeFromPtr(p capnp.Ptr) SoilCharacteristicModifier {
	return SoilCharacteristicModifier(capnp.Struct{}.DecodeFromPtr(p))
}

func (s SoilCharacteristicModifier) ToPtr() capnp.Ptr {
	return capnp.Struct(s).ToPtr()
}
func (s SoilCharacteristicModifier) IsValid() bool {
	return capnp.Struct(s).IsValid()
}

func (s SoilCharacteristicModifier) Message() *capnp.Message {
	return capnp.Struct(s).Message()
}

func (s SoilCharacteristicModifier) Segment() *capnp.Segment {
	return capnp.Struct(s).Segment()
}
func (s SoilCharacteristicModifier) List() (SoilCharacteristicModifier_Data_List, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return SoilCharacteristicModifier_Data_List(p.List()), err
}

func (s SoilCharacteristicModifier) HasList() bool {
	return capnp.Struct(s).HasPtr(0)
}

func (s SoilCharacteristicModifier) SetList(v SoilCharacteristicModifier_Data_List) error {
	return capnp.Struct(s).SetPtr(0, v.ToPtr())
}

// NewList sets the list field to a newly
// allocated SoilCharacteristicModifier_Data_List, preferring placement in s's segment.
func (s SoilCharacteristicModifier) NewList(n int32) (SoilCharacteristicModifier_Data_List, error) {
	l, err := NewSoilCharacteristicModifier_Data_List(capnp.Struct(s).Segment(), n)
	if err != nil {
		return SoilCharacteristicModifier_Data_List{}, err
	}
	err = capnp.Struct(s).SetPtr(0, l.ToPtr())
	return l, err
}

// SoilCharacteristicModifier_List is a list of SoilCharacteristicModifier.
type SoilCharacteristicModifier_List = capnp.StructList[SoilCharacteristicModifier]

// NewSoilCharacteristicModifier creates a new list of SoilCharacteristicModifier.
func NewSoilCharacteristicModifier_List(s *capnp.Segment, sz int32) (SoilCharacteristicModifier_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1}, sz)
	return capnp.StructList[SoilCharacteristicModifier](l), err
}

// SoilCharacteristicModifier_Future is a wrapper for a SoilCharacteristicModifier promised by a client call.
type SoilCharacteristicModifier_Future struct{ *capnp.Future }

func (f SoilCharacteristicModifier_Future) Struct() (SoilCharacteristicModifier, error) {
	p, err := f.Future.Ptr()
	return SoilCharacteristicModifier(p.Struct()), err
}

type SoilCharacteristicModifier_Data capnp.Struct

// SoilCharacteristicModifier_Data_TypeID is the unique identifier for the type SoilCharacteristicModifier_Data.
const SoilCharacteristicModifier_Data_TypeID = 0xa968a46ccde8b1b4

func NewSoilCharacteristicModifier_Data(s *capnp.Segment) (SoilCharacteristicModifier_Data, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	return SoilCharacteristicModifier_Data(st), err
}

func NewRootSoilCharacteristicModifier_Data(s *capnp.Segment) (SoilCharacteristicModifier_Data, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	return SoilCharacteristicModifier_Data(st), err
}

func ReadRootSoilCharacteristicModifier_Data(msg *capnp.Message) (SoilCharacteristicModifier_Data, error) {
	root, err := msg.Root()
	return SoilCharacteristicModifier_Data(root.Struct()), err
}

func (s SoilCharacteristicModifier_Data) String() string {
	str, _ := text.Marshal(0xa968a46ccde8b1b4, capnp.Struct(s))
	return str
}

func (s SoilCharacteristicModifier_Data) EncodeAsPtr(seg *capnp.Segment) capnp.Ptr {
	return capnp.Struct(s).EncodeAsPtr(seg)
}

func (SoilCharacteristicModifier_Data) DecodeFromPtr(p capnp.Ptr) SoilCharacteristicModifier_Data {
	return SoilCharacteristicModifier_Data(capnp.Struct{}.DecodeFromPtr(p))
}

func (s SoilCharacteristicModifier_Data) ToPtr() capnp.Ptr {
	return capnp.Struct(s).ToPtr()
}
func (s SoilCharacteristicModifier_Data) IsValid() bool {
	return capnp.Struct(s).IsValid()
}

func (s SoilCharacteristicModifier_Data) Message() *capnp.Message {
	return capnp.Struct(s).Message()
}

func (s SoilCharacteristicModifier_Data) Segment() *capnp.Segment {
	return capnp.Struct(s).Segment()
}
func (s SoilCharacteristicModifier_Data) SoilType() (string, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return p.Text(), err
}

func (s SoilCharacteristicModifier_Data) HasSoilType() bool {
	return capnp.Struct(s).HasPtr(0)
}

func (s SoilCharacteristicModifier_Data) SoilTypeBytes() ([]byte, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return p.TextBytes(), err
}

func (s SoilCharacteristicModifier_Data) SetSoilType(v string) error {
	return capnp.Struct(s).SetText(0, v)
}

func (s SoilCharacteristicModifier_Data) OrganicMatter() float32 {
	return math.Float32frombits(capnp.Struct(s).Uint32(0))
}

func (s SoilCharacteristicModifier_Data) SetOrganicMatter(v float32) {
	capnp.Struct(s).SetUint32(0, math.Float32bits(v))
}

func (s SoilCharacteristicModifier_Data) AirCapacity() int8 {
	return int8(capnp.Struct(s).Uint8(4))
}

func (s SoilCharacteristicModifier_Data) SetAirCapacity(v int8) {
	capnp.Struct(s).SetUint8(4, uint8(v))
}

func (s SoilCharacteristicModifier_Data) FieldCapacity() int8 {
	return int8(capnp.Struct(s).Uint8(5))
}

func (s SoilCharacteristicModifier_Data) SetFieldCapacity(v int8) {
	capnp.Struct(s).SetUint8(5, uint8(v))
}

func (s SoilCharacteristicModifier_Data) NFieldCapacity() int8 {
	return int8(capnp.Struct(s).Uint8(6))
}

func (s SoilCharacteristicModifier_Data) SetNFieldCapacity(v int8) {
	capnp.Struct(s).SetUint8(6, uint8(v))
}

// SoilCharacteristicModifier_Data_List is a list of SoilCharacteristicModifier_Data.
type SoilCharacteristicModifier_Data_List = capnp.StructList[SoilCharacteristicModifier_Data]

// NewSoilCharacteristicModifier_Data creates a new list of SoilCharacteristicModifier_Data.
func NewSoilCharacteristicModifier_Data_List(s *capnp.Segment, sz int32) (SoilCharacteristicModifier_Data_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1}, sz)
	return capnp.StructList[SoilCharacteristicModifier_Data](l), err
}

// SoilCharacteristicModifier_Data_Future is a wrapper for a SoilCharacteristicModifier_Data promised by a client call.
type SoilCharacteristicModifier_Data_Future struct{ *capnp.Future }

func (f SoilCharacteristicModifier_Data_Future) Struct() (SoilCharacteristicModifier_Data, error) {
	p, err := f.Future.Ptr()
	return SoilCharacteristicModifier_Data(p.Struct()), err
}

type CapillaryRiseRate capnp.Struct

// CapillaryRiseRate_TypeID is the unique identifier for the type CapillaryRiseRate.
const CapillaryRiseRate_TypeID = 0x9b169bc96bb3d24b

func NewCapillaryRiseRate(s *capnp.Segment) (CapillaryRiseRate, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1})
	return CapillaryRiseRate(st), err
}

func NewRootCapillaryRiseRate(s *capnp.Segment) (CapillaryRiseRate, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1})
	return CapillaryRiseRate(st), err
}

func ReadRootCapillaryRiseRate(msg *capnp.Message) (CapillaryRiseRate, error) {
	root, err := msg.Root()
	return CapillaryRiseRate(root.Struct()), err
}

func (s CapillaryRiseRate) String() string {
	str, _ := text.Marshal(0x9b169bc96bb3d24b, capnp.Struct(s))
	return str
}

func (s CapillaryRiseRate) EncodeAsPtr(seg *capnp.Segment) capnp.Ptr {
	return capnp.Struct(s).EncodeAsPtr(seg)
}

func (CapillaryRiseRate) DecodeFromPtr(p capnp.Ptr) CapillaryRiseRate {
	return CapillaryRiseRate(capnp.Struct{}.DecodeFromPtr(p))
}

func (s CapillaryRiseRate) ToPtr() capnp.Ptr {
	return capnp.Struct(s).ToPtr()
}
func (s CapillaryRiseRate) IsValid() bool {
	return capnp.Struct(s).IsValid()
}

func (s CapillaryRiseRate) Message() *capnp.Message {
	return capnp.Struct(s).Message()
}

func (s CapillaryRiseRate) Segment() *capnp.Segment {
	return capnp.Struct(s).Segment()
}
func (s CapillaryRiseRate) List() (CapillaryRiseRate_Data_List, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return CapillaryRiseRate_Data_List(p.List()), err
}

func (s CapillaryRiseRate) HasList() bool {
	return capnp.Struct(s).HasPtr(0)
}

func (s CapillaryRiseRate) SetList(v CapillaryRiseRate_Data_List) error {
	return capnp.Struct(s).SetPtr(0, v.ToPtr())
}

// NewList sets the list field to a newly
// allocated CapillaryRiseRate_Data_List, preferring placement in s's segment.
func (s CapillaryRiseRate) NewList(n int32) (CapillaryRiseRate_Data_List, error) {
	l, err := NewCapillaryRiseRate_Data_List(capnp.Struct(s).Segment(), n)
	if err != nil {
		return CapillaryRiseRate_Data_List{}, err
	}
	err = capnp.Struct(s).SetPtr(0, l.ToPtr())
	return l, err
}

// CapillaryRiseRate_List is a list of CapillaryRiseRate.
type CapillaryRiseRate_List = capnp.StructList[CapillaryRiseRate]

// NewCapillaryRiseRate creates a new list of CapillaryRiseRate.
func NewCapillaryRiseRate_List(s *capnp.Segment, sz int32) (CapillaryRiseRate_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 0, PointerCount: 1}, sz)
	return capnp.StructList[CapillaryRiseRate](l), err
}

// CapillaryRiseRate_Future is a wrapper for a CapillaryRiseRate promised by a client call.
type CapillaryRiseRate_Future struct{ *capnp.Future }

func (f CapillaryRiseRate_Future) Struct() (CapillaryRiseRate, error) {
	p, err := f.Future.Ptr()
	return CapillaryRiseRate(p.Struct()), err
}

type CapillaryRiseRate_Data capnp.Struct

// CapillaryRiseRate_Data_TypeID is the unique identifier for the type CapillaryRiseRate_Data.
const CapillaryRiseRate_Data_TypeID = 0xb78a89c58fad885d

func NewCapillaryRiseRate_Data(s *capnp.Segment) (CapillaryRiseRate_Data, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	return CapillaryRiseRate_Data(st), err
}

func NewRootCapillaryRiseRate_Data(s *capnp.Segment) (CapillaryRiseRate_Data, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	return CapillaryRiseRate_Data(st), err
}

func ReadRootCapillaryRiseRate_Data(msg *capnp.Message) (CapillaryRiseRate_Data, error) {
	root, err := msg.Root()
	return CapillaryRiseRate_Data(root.Struct()), err
}

func (s CapillaryRiseRate_Data) String() string {
	str, _ := text.Marshal(0xb78a89c58fad885d, capnp.Struct(s))
	return str
}

func (s CapillaryRiseRate_Data) EncodeAsPtr(seg *capnp.Segment) capnp.Ptr {
	return capnp.Struct(s).EncodeAsPtr(seg)
}

func (CapillaryRiseRate_Data) DecodeFromPtr(p capnp.Ptr) CapillaryRiseRate_Data {
	return CapillaryRiseRate_Data(capnp.Struct{}.DecodeFromPtr(p))
}

func (s CapillaryRiseRate_Data) ToPtr() capnp.Ptr {
	return capnp.Struct(s).ToPtr()
}
func (s CapillaryRiseRate_Data) IsValid() bool {
	return capnp.Struct(s).IsValid()
}

func (s CapillaryRiseRate_Data) Message() *capnp.Message {
	return capnp.Struct(s).Message()
}

func (s CapillaryRiseRate_Data) Segment() *capnp.Segment {
	return capnp.Struct(s).Segment()
}
func (s CapillaryRiseRate_Data) SoilType() (string, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return p.Text(), err
}

func (s CapillaryRiseRate_Data) HasSoilType() bool {
	return capnp.Struct(s).HasPtr(0)
}

func (s CapillaryRiseRate_Data) SoilTypeBytes() ([]byte, error) {
	p, err := capnp.Struct(s).Ptr(0)
	return p.TextBytes(), err
}

func (s CapillaryRiseRate_Data) SetSoilType(v string) error {
	return capnp.Struct(s).SetText(0, v)
}

func (s CapillaryRiseRate_Data) Distance() uint8 {
	return capnp.Struct(s).Uint8(0)
}

func (s CapillaryRiseRate_Data) SetDistance(v uint8) {
	capnp.Struct(s).SetUint8(0, v)
}

func (s CapillaryRiseRate_Data) Rate() float32 {
	return math.Float32frombits(capnp.Struct(s).Uint32(4))
}

func (s CapillaryRiseRate_Data) SetRate(v float32) {
	capnp.Struct(s).SetUint32(4, math.Float32bits(v))
}

// CapillaryRiseRate_Data_List is a list of CapillaryRiseRate_Data.
type CapillaryRiseRate_Data_List = capnp.StructList[CapillaryRiseRate_Data]

// NewCapillaryRiseRate_Data creates a new list of CapillaryRiseRate_Data.
func NewCapillaryRiseRate_Data_List(s *capnp.Segment, sz int32) (CapillaryRiseRate_Data_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1}, sz)
	return capnp.StructList[CapillaryRiseRate_Data](l), err
}

// CapillaryRiseRate_Data_Future is a wrapper for a CapillaryRiseRate_Data promised by a client call.
type CapillaryRiseRate_Data_Future struct{ *capnp.Future }

func (f CapillaryRiseRate_Data_Future) Struct() (CapillaryRiseRate_Data, error) {
	p, err := f.Future.Ptr()
	return CapillaryRiseRate_Data(p.Struct()), err
}

const schema_f83caca0747996ab = "x\xda\x94T\xc1k\x13O\x18\xfd\xde\xcc$\xf9\xfdJ" +
	"\xfb\xcbo\xdd\xa0\xc7@\xa9\x94\x16,\x15o\xa2DI" +
	"\xea\xa1Z\xc9\xb4\x16\x15\x14\x19\xb7[;\x1a\x93ew" +
	"ER\xf4 Xh\xc5\xa2\x88\x8aP\x85\x1e<X\xaa" +
	"\xa8(x\x10\x8f=\x88x\xf1\xea\xc5\x83\x82\xe8?\xa0" +
	"\"\xacL\xd2n\xa2M\xa5\xbd\x0do\xbe\xf9\xbe\xf7\xbd" +
	"\xf7v\xfb\xdf`\x8f\xd8\xde\xd1-\x88\xc9\xfeD2\xda" +
	"\xff\xee\xd9\x99\xd7s\x9b\xe7\xc8\xda\x84h\xf1v5\x9c" +
	"\x7f\xb8\xeb\x1b%\x90\"\xda\xf1\x1d\x9d\xb0\xffe[\x88" +
	"l\x8b\xe5\x08\xd1\xf3\xa7\x9f\xdf\x96\xeeO,\x90\xdc\x06" +
	"D#/?=\x99k\xfb\xfaq\xb9z/\xbb\x01\xfb" +
	"(3\xc7Q\x96\x05!:>\xfd\xe8\xda\xd2\xcc\x95\x17" +
	"$\xbb\x80\xc6\xa4zy\x95\x0f\xc2\x9e\xe5)\"{\x86" +
	"?\xa6\xa6v-\x98\xf4\x88\xd3\xb0w\x0b\xc3d@\x18" +
	"&\xce\xfb\xad\x1f\x0e/\xfe\xf8B\xb2\x07\x88.u\x1e" +
	"\xec\xef\xee\x9c\xf8\xb9\\}N\xf8\xb0g\x849N\x89" +
	"\x1a\x93\xb8\xa0E\xef\x85\xc4 \xecW\x09\xd3{)\x91" +
	"\xa3|\x14Tt\xe9\x84\xa7|\xae\xce\x06}\x8e\xf2\xca" +
	"\xde\xce\xbc\xf2t\xa9\xa4\xfc\xea\xb0\x0e\xdc\xe1\x94\x0a]" +
	")\xd0\xb4\xa0\x85\xdetA\x85J\x0a.\x88\x04\x88\xac" +
	"\x8e^\"\xf9\x0f\x87\xecbH\x97t\x10\xe2?B\x91" +
	"\x03\xff7\x9e\x11\x0c\x18\x0fL4\x06\x8eTt)?" +
	"\xa1|\xe5\x84\xae\xaf\x83P;C\x951=\xae]\xbf" +
	"\xaf\xa0B\xa8\" 3\xf1\xac\x8b\x83D\xf2\x02\x87\x9c" +
	"f\x0020\xd8\x94O$/s\xc8\xeb\x0c\x16\x13\x19" +
	"0\"k\xf6$\x91\xbc\xca!\xef0X<\x91\x01'" +
	"\xb2n\x99\xca\x9b\x1cr\x9e\xc1\x12\xc9\x0c\x04\x91uo" +
	"\x92H\xde\xe5\x90\x0fX\x9d\xe0\xa1\xaa\xe7\x12\x11\xda\x89" +
	"\xa1\x9d\x10U\xfcS\xaa\xac\x9d!\xca\xaa0t}\xb4" +
	"\x11C\x1b!R\xda\xcf+O9\x94\xd2a\x15\x8c\x18" +
	"\x18!\x1a\xd7ni,\xaf<\xca*\xa7\x19/\xef\xab" +
	"_P\xce\xfb\xfdbE\x13\xb1\x96\x09*t\x8d\x14\x8a" +
	"\xc8h\xd1\x1ek1`\xb4(p\xc8bC\x8b!\x83" +
	"\x1d\xe0\x90G\x8c\x16\xa8k1j\x0c*r\xc8ck" +
	"l8\xa6\x83P\x95\x9d\x1a\x96$\x86$!\xed\xab\xd0" +
	"\x8dWm\xc1\xb1\xb5oic\\-1\xf1\x17\xb4\xb1" +
	"\xc4\xc4\xcf\xfeH\xcc_'\x9b\xf6\xd9\x9aF\xebH\xcb" +
	"dsZX\xab\xb4\xf0Vi\x11\xebL\x8b\xc1\x86\xd5" +
	"\xf9\x02\xe5\xdcr`|\xe6\xc4\xc0W\xc5eY\xe6U" +
	"qY\xc1W\xc5e\xe5b\xdd\x82\x10\xd5|\x88\xff\x1f" +
	"\x1b\xf3!~V\xf7\xe1W\x00\x00\x00\xff\xffQ\xc9`" +
	"\x8e"

func RegisterSchema(reg *schemas.Registry) {
	reg.Register(&schemas.Schema{
		String: schema_f83caca0747996ab,
		Nodes: []uint64{
			0x9b169bc96bb3d24b,
			0xa968a46ccde8b1b4,
			0xb78a89c58fad885d,
			0xe4eb0a9bb0e5bb53,
			0xeafaab57e025db63,
			0xfc682227304e2281,
		},
		Compressed: true,
	})
}
