# Changelog

## [0.1.41](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.40...v0.1.41) (2025-11-19)


### Features

* add proper _context methods ([e342e9a](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/e342e9ae714ad7df8dc44e09032d566167559285))
* add result types to top level ([5cc0977](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/5cc09777e534bc1151fc23722b329d0ec27b8098))
* almost feature complete ([52302bb](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/52302bb33f4c7be290c616d9936491aa8e37cb6b))
* expand the request object ([10e1442](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/10e1442a72bd90a262a7b15e034957bfbc6344e5))
* explicit default values for primitives according to capnp ([8b6f365](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/8b6f3655dcc8d9a0cd94e394753c1b2a216a04ab))
* fix _CapabilityClient typing and overloads and improve enum typing ([1f1198d](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/1f1198d52fb9ba2ada4d97280653d137996705cb))
* move in augmented stubs package and update python stubs ([e6ee1d8](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/e6ee1d89b36981e8800d55c9da371510c6c95ca4))
* proper generic handling for structs and use modern type aliases in many more places ([3f59b64](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/3f59b64c85ce1ff09bfc1745316441a5e2bbea4a))


### Bug Fixes

* recompile to allow None returns on server and have optional parameter values ([9e5a62c](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/9e5a62c558d20eb7de1f639864a892e80155e6d5))
* small issues and move back to Sequence for now ([1db4fad](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/1db4fad1f268bad03a77f50b446ae0261900daba))
* sorting of decorators ([a5582c2](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/a5582c20d5a16e68b8681085f600a49ea58b548d))

## [0.1.40](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.39...v0.1.40) (2025-11-06)


### Bug Fixes

* try to fix project structure to not get confused with the relative imports of the pycapnp files ([3012ff5](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/3012ff5870317212908b4648125f36c148bf3f42))

## [0.1.39](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.38...v0.1.39) (2025-11-06)


### Features

* add additional package for schemas with stubs for type checking… ([#14](https://github.com/zalf-rpm/mas_capnproto_schemas/issues/14)) ([8814246](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/88142462fc1ecd0c483fdacc0b0258e17dc0e0b2))

## [0.1.38](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.37...v0.1.38) (2025-11-04)


### Features

* removed commented interface ([57d1864](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/57d186455b31846ef5ae965a6b7046a0bd8190cc))

## [0.1.37](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.36...v0.1.37) (2025-09-29)


### Features

* added potET to climate variables ([61cd28b](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/61cd28bc46a4aa4e5b762b6df135bd1cfb4de1e0))
* basic recompilation in docker image and ([#10](https://github.com/zalf-rpm/mas_capnproto_schemas/issues/10)) ([8036c4c](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/8036c4c17e56dbbf36cb2e753bc92eb485f976c1))

## [0.1.36](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.35...v0.1.36) (2025-09-10)


### Features

* added DefaultConfig option to FBP component ([ddd976b](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/ddd976ba1401552b5bceddc4471655735da4dfeb))
* simplify import logic  ([#9](https://github.com/zalf-rpm/mas_capnproto_schemas/issues/9)) ([6891b3a](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/6891b3ac5b121958e255ff976c9bfb8e3b59e59b))

## [0.1.35](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.34...v0.1.35) (2025-08-29)


### Features

* add release please action and config to publish to pypi and cre… ([100a89d](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/100a89dc9da6fe20738cdba35ce0fd6a32b448af))
* add release please action and config to publish to pypi and create releases ([0dcb556](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/0dcb55622acf011530a6dd6eb7c3a4800208157b))
* **CD:** release on regular pypi instead of test.pypi ([15a65a7](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/15a65a76402059ae354378298452fb3161747271))
* **script:** add configurable python compile script ([#1](https://github.com/zalf-rpm/mas_capnproto_schemas/issues/1)) ([b645fa3](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/b645fa386092972cec8a7592c762957df6ae478a))
* switch to pep-621 compliant pyproject.toml storing project metadata under [project] ([e7040a8](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/e7040a887a364b0e4d6c44ac9e183c22bcf6467d))
* switch to pep-621 compliant pyproject.toml storing project metadata under [project] ([550195e](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/550195ec32158cc8570062266eebe9f88e261b7a))


### Bug Fixes

* populate readme to prevent push to pypi 400 error ([bcd3d35](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/bcd3d359f41b2e9dbf32ed39a311e08cefec0e71))

## [0.1.32](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.31...v0.1.32) (2025-08-22)


### Bug Fixes

* populate readme to prevent push to pypi 400 error ([bcd3d35](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/bcd3d359f41b2e9dbf32ed39a311e08cefec0e71))

## [0.1.31](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.30...v0.1.31) (2025-08-22)


### Features

* add release please action and config to publish to pypi and cre… ([100a89d](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/100a89dc9da6fe20738cdba35ce0fd6a32b448af))
* add release please action and config to publish to pypi and create releases ([0dcb556](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/0dcb55622acf011530a6dd6eb7c3a4800208157b))
* **script:** add configurable python compile script ([#1](https://github.com/zalf-rpm/mas_capnproto_schemas/issues/1)) ([b645fa3](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/b645fa386092972cec8a7592c762957df6ae478a))
* switch to pep-621 compliant pyproject.toml storing project metadata under [project] ([e7040a8](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/e7040a887a364b0e4d6c44ac9e183c22bcf6467d))
* switch to pep-621 compliant pyproject.toml storing project metadata under [project] ([550195e](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/550195ec32158cc8570062266eebe9f88e261b7a))
