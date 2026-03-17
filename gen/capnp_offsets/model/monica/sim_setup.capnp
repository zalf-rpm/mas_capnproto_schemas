# model/monica/sim_setup.capnp
@0xac57747d36fdd0b1;
struct Setup @0xa4b1a2ad9a77fdc7 {  # 24 bytes, 10 ptrs
  runId @0 :Int64;  # bits[0, 64)
  sowingTime @1 :Text;  # ptr[0]
  harvestTime @2 :Text;  # ptr[1]
  cropId @3 :Text;  # ptr[2]
  simJson @4 :Text;  # ptr[3]
  cropJson @5 :Text;  # ptr[4]
  siteJson @6 :Text;  # ptr[5]
  startDate @7 :Text;  # ptr[6]
  endDate @8 :Text;  # ptr[7]
  groundwaterLevel @9 :Bool;  # bits[64, 65)
  impenetrableLayer @10 :Bool;  # bits[65, 66)
  elevation @11 :Bool;  # bits[66, 67)
  slope @12 :Bool;  # bits[67, 68)
  latitude @13 :Bool;  # bits[68, 69)
  landcover @14 :Bool;  # bits[69, 70)
  fertilization @15 :Bool;  # bits[70, 71)
  nitrogenResponseOn @16 :Bool;  # bits[71, 72)
  irrigation @17 :Bool;  # bits[72, 73)
  waterDeficitResponseOn @18 :Bool;  # bits[73, 74)
  emergenceMoistureControlOn @19 :Bool;  # bits[74, 75)
  emergenceFloodingControlOn @20 :Bool;  # bits[75, 76)
  leafExtensionModifier @21 :Bool;  # bits[76, 77)
  co2 @22 :Float32;  # bits[96, 128)
  o3 @23 :Float32;  # bits[128, 160)
  fieldConditionModifier @24 :Float32;  # bits[160, 192)
  stageTemperatureSum @25 :Text;  # ptr[8]
  useVernalisationFix @26 :Bool;  # bits[77, 78)
  comment @27 :Text;  # ptr[9]
}
