# Changelog

## [0.1.49](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.48...v0.1.49) (2026-02-24)


### Features

* made defaultConfig StructuredText ([98a02b6](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/98a02b6f915747ce3da1f374cab5b00e68cf9a53))

## [0.1.48](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.47...v0.1.48) (2026-01-19)


### Features

* add secretSeed param to gateway register method to have stable adresses if needed ([f16f5e5](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/f16f5e56e4d4d7f88553a2b4720e062482363586))

## [0.1.47](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.46...v0.1.47) (2026-01-15)


### Bug Fixes

* run with fixed generator including the proper stubs to augment ([8c96f2d](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/8c96f2d27fddca00cc4a850ecaa9ad61fdaf63cb))

## [0.1.46](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.45...v0.1.46) (2026-01-14)


### Features

* add capnp offset generation to unified script and github action ([4b442ff](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/4b442ffe6934ffd9a4e197992cd058cc3fafe79c))
* add modam service for dakis ([4878108](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/487810886efe7ff987cb8dfceea70b04b8355f61))
* Add python and restructure schemas base dir ([#25](https://github.com/zalf-rpm/mas_capnproto_schemas/issues/25)) ([2f9e992](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/2f9e9922793a0ab5b8e30b0402d2306086693653))
* differentiate the different model types to run ([fd8e878](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/fd8e878f419d979fdab80ed89ea7e0a8867d1fa2))


### Bug Fixes

* use shared schema loader ([30f3b64](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/30f3b64fd82fb9781ffb6868f946462fc73090c3))

## [0.1.45](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.44...v0.1.45) (2025-12-05)


### Features

* udpate dockerfile and workflow to incorporate the fixed csharp compiler ([4938c37](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/4938c37c3454629f3e2cf7e9f623e40aa8de411e))


### Bug Fixes

* change kwargs type to any and ass ssl context ([174539e](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/174539ea9699df5014a8118034bea705e4d900b8))
* generic param for Capability must have slipped through some testing ([00bc048](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/00bc048d90b64ea254fad7d7b8dfee121cb78631))

## [0.1.44](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.43...v0.1.44) (2025-11-25)


### Features

* add proper AnyPointer, AnyStruct, AnyList and Capability handling ([2cbc33e](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/2cbc33e379b5b67199c40762734d7a27b9afab64))
* add proper list builders and reader ([232047d](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/232047d2955341c5b983c6052a22d1c4b6766aed))
* add top level server types ([f0c66c4](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/f0c66c4338644725b5702599a2fc983e338279fb))
* flesh out module names and align generated better to base stubs. ([06eadac](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/06eadac7234f6b760f3bc8903d14d4150717da08))
* flesh out the _Schema types ([6245dad](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/6245dadc1cebaa2c9d63fd1e22be9e262cedc67e))
* for plain struct context.results return the builder isntance of the struct ([3b76c9b](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/3b76c9b2bfb0f7c9ec5145299d0a26e126988436))


### Bug Fixes

* added missing RunnableFactory ([b4b3f02](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/b4b3f021fb9a89f84a4e35bf6319490f50b75af7))
* imported type aliases ([d95d8a9](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/d95d8a97007182b9f1bd0557867e90ccef80e6a5))
* proper readers and builders ([afff8a1](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/afff8a13659f77939a820de4272d84e4949f1a21))
* Single value return for AnyTypes ([5729b6b](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/5729b6b676c86468f166b434d2ca239290475355))

## [0.1.43](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.42...v0.1.43) (2025-11-20)


### Bug Fixes

* regenerate with including parent dir in input path to resolve imports without id issues ([4dc18b5](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/4dc18b5349b625680682eddb21b065e9c7b3cf90))

## [0.1.42](https://github.com/zalf-rpm/mas_capnproto_schemas/compare/v0.1.41...v0.1.42) (2025-11-20)


### Bug Fixes

* regenerate python stubs with correct import paths ([5ad4dca](https://github.com/zalf-rpm/mas_capnproto_schemas/commit/5ad4dca094f55ea718bc46ea29d2f2b9568001fa))

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
