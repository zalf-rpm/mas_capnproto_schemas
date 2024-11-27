module github.com/zalf-rpm/mas-infrastructure/capnproto_schemas/gen/go/common

go 1.19

require capnproto.org/go/capnp/v3 v3.0.1-alpha.2

replace github.com/zalf-rpm/mas-infrastructure/capnproto_schemas/gen/go/persistence => ../persistence

require (
	github.com/colega/zeropool v0.0.0-20230505084239-6fb4a4f75381 // indirect
	golang.org/x/sync v0.8.0 // indirect
)