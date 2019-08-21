import GUI as gui
from tkinter import *

gta5config = '''
<?xml version="1.0" encoding="UTF-8"?>

<!--
DILAPIDATED-REALISM DISPATCH ENHANCED 4.0
 gameconfig.xml
 
 RE by: alexguiree, CamxxCore, and Dilapidated 
 Assistance from: Unknown, PNWParksFan, Cass, Jax765, and the RDE Team

If RPH freezes immediately when you try to list vehicle models 
(e.g. with console command SpawnAndWarp), search for fwArchetypePooledMap
in this file and decrease the value.
-->

<fwAllConfigs>
	<ConfigArray>

		<!-- Base configuration, applies to all platforms and builds. -->
		<Item>
			<Build>Any</Build>
			<Platforms>Any</Platforms>
			<Config type="CGameConfig">
				<PoolSizes>
					<Entries>
						<!-- START: Values here were found in GTA5.exe and can be added to this xml 
						For more info view the bottom of this xml or research these pastebins https://pastebin.com/Ah3w4mPm and https://pastebin.com/ay5avz3y -->
						<Item>
							<!-- R* cap = 7 : Affects Swat Rope Rappel AI -->
							<PoolName>ropedata</PoolName>
							<PoolSize value="28"/>
						</Item>
						<Item>
							<!-- R* cap = 111 : Affects CAmbulanceOrder CFireOrder CGangOrder CPoliceOrder CSwatOrder etc -->
							<PoolName>orders</PoolName>
							<PoolSize value="444"/>
						</Item>
						<Item>
							<!-- R* cap = 51 : Affects CArrestIncident CScriptIncident CWantedIncident etc -->
							<PoolName>incidents</PoolName>
							<PoolSize value="204"/>
						</Item>
						<Item>
							<!-- R* cap = 4 : Affects limits of total caihandling parameters in vehicleaihandlinginfo.meta (you can now have as many custom handlinginfo parameters as you wish)-->
							<PoolName>caihandlinginfo</PoolName>
							<PoolSize value="12"/>
						</Item>
						<Item>
							<!-- R* cap = 36 : Affects limits of total curvepoint parameters in vehicleaihandlinginfo.meta (you can now have as many custom curvepoint parameters as you wish)-->
							<PoolName>caicurvepoint</PoolName>
							<PoolSize value="108"/>
						</Item>
						<Item>
							<!-- R* cap = 1600 : Unknown usage-->
							<PoolName>fraginstgta</PoolName>
							<PoolSize value="5000"/>
						</Item>				
						<Item>
							<!-- R* cap = 31 : Increasing this value in addition to CEvent can resolve GTA.Native.?A0x55605b1d.NativeTask.Run() crashes in wineventlog -->
							<PoolName>ctasksequencelist</PoolName>
							<PoolSize value="200"/>
						</Item>				
						<Item>
							<!-- R* cap = 83 : Unknown usage-->
							<PoolName>cgamescripthandler</PoolName>
							<PoolSize value="400"/>
						</Item>
						<Item>
							<!-- R* cap = 220 : Unknown usage-->
							<PoolName>cweaponcomponent</PoolName>
							<PoolSize value="440"/>
						</Item>
						<Item>
							<!-- R* cap = 410 : Unknown usage-->
							<PoolName>cweaponcomponentinfo</PoolName>
							<PoolSize value="820"/>
						</Item>	
						<Item>
							<!-- R* cap = 33 : Unknown usage-->
							<PoolName>cplayerinfo</PoolName>
							<PoolSize value="132"/>
						</Item>						
						<Item>
							<!-- R* cap = 60 : Unknown usage-->
							<PoolName>cvehiclestreamrequestgfx</PoolName>
							<PoolSize value="240"/>
						</Item>						
						<Item>
							<!-- R* cap = 100 : Unknown usage-->
							<PoolName>cvehiclestreamrendergfx</PoolName>
							<PoolSize value="400"/>
						</Item>								
						<Item>
							<!-- R* cap = 1500 : Unknown usage-->
							<PoolName>wheels</PoolName>
							<PoolSize value="3000"/>
						</Item>						
						<Item>
							<!-- R* cap = 1250 : Unknown usage-->
							<PoolName>chandlingobject</PoolName>
							<PoolSize value="2500"/>
						</Item>								
						<Item>
							<!-- R* cap = 100 : Unknown usage-->
							<PoolName>cpatrollink</PoolName>
							<PoolSize value="400"/>
						</Item>						
						<Item>
							<!-- R* cap = 50 : Unknown usage-->
							<PoolName>cpatrolnode</PoolName>
							<PoolSize value="200"/>
						</Item>						
						<Item>
							<!-- R* cap = 6 : Unknown usage-->
							<PoolName>patrolroute</PoolName>
							<PoolSize value="24"/>
						</Item>								
						<Item>
							<!-- R* cap = 36 : Unknown usage-->
							<PoolName>cnamedpatrolroute</PoolName>
							<PoolSize value="144"/>
						</Item>						
						<Item>
							<!-- R* cap = 40 : Unknown usage-->
							<PoolName>pointroute</PoolName>
							<PoolSize value="160"/>
						</Item>						
						<Item>
							<!-- R* cap = 255 : Unknown usage-->
							<PoolName>cspawnpointoverrideextension</PoolName>
							<PoolSize value="510"/>
						</Item>						
						<Item>
							<!-- R* cap = 4 : Unknown usage-->
							<PoolName>ccollectioninfo</PoolName>
							<PoolSize value="16"/>
						</Item>								
						<Item>
							<!-- R* cap = 1200 : Unknown usage-->
							<PoolName>tasksequenceinfo</PoolName>
							<PoolSize value="4800"/>
						</Item>								
						<Item>
							<!-- R* cap = 3 : Unknown usage-->
							<PoolName>ceventdecisionmakermodifiablecomponent</PoolName>
							<PoolSize value="12"/>
						</Item>						
						<Item>
							<!-- R* cap = 25 : Unknown usage-->
							<PoolName>ceventdecisionmaker</PoolName>
							<PoolSize value="100"/>
						</Item>									
						<Item>
							<!-- R* cap = 900 : Unknown usage-->
							<PoolName>cscenariopoint</PoolName>
							<PoolSize value="1800"/>
						</Item>
						<Item>
							<!-- R* cap = 300 : Unknown usage-->
							<PoolName>crelationshipgroup</PoolName>
							<PoolSize value="600"/>
						</Item>
						<Item>
							<!-- R* cap = 128 : Unknown usage-->
							<PoolName>vehicleglasscomponententity</PoolName>
							<PoolSize value="256"/>
						</Item>
						<Item>
							<!-- R* cap = 128 : Unknown usage-->
							<PoolName>targetting</PoolName>
							<PoolSize value="256"/>
						</Item>
						<Item>
							<!-- R* cap = 512 : Unknown usage-->
							<PoolName>naenvironmentgroup</PoolName>
							<PoolSize value="1024"/>
						</Item>
						<Item>
							<!-- R* cap = 50 : Unknown usage-->
							<PoolName>pedprop req data</PoolName>
							<PoolSize value="200"/>
						</Item>
						<Item>
							<!-- R* cap = 120 : Unknown usage-->
							<PoolName>pedprop render data</PoolName>
							<PoolSize value="480"/>
						</Item>
						<Item>
							<!-- R* cap = 45 : Unknown usage-->
							<PoolName>streamped req data</PoolName>
							<PoolSize value="180"/>
						</Item>
						<Item>
							<!-- R* cap = 100 : Unknown usage-->
							<PoolName>streamped render data</PoolName>
							<PoolSize value="400"/>
						</Item>
						<Item>
							<!-- R* cap = 60 : Unknown usage-->
							<PoolName>cbullet</PoolName>
							<PoolSize value="240"/>
						</Item>
						<Item>
							<!-- R* cap = 128 : Unknown usage-->
							<PoolName>cbullet::sbulletinstance</PoolName>
							<PoolSize value="512"/>
						</Item>
						<Item>
							<!-- R* cap = 104 : Unknown usage-->
							<PoolName>fwcontainerlod</PoolName>
							<PoolSize value="208"/>
						</Item>
						<Item>
							<!-- R* cap = 700 : Unknown usage-->
							<PoolName>fwscriptguid</PoolName>
							<PoolSize value="2800"/>
						</Item>
						<Item>
							<!-- R* cap = 128 : Unknown usage-->
							<PoolName>itemsetbuffer</PoolName>
							<PoolSize value="266"/>
						</Item>
						<Item>
							<!-- R* cap = 600 : Unknown usage-->
							<PoolName>decorator</PoolName>
							<PoolSize value="600"/>
						</Item>						
						<!-- END -->

						
						<!-- Keep these sorted -->
						<Item>
							<PoolName>AnimatedBuilding</PoolName>
							<PoolSize value="1200"/>
						</Item>
						<Item>
							<PoolName>AttachmentExtension</PoolName>
							<PoolSize value="430"/>
						</Item>
						<Item>
						  <PoolName>AudioHeap</PoolName>
						  <PoolSize value="195"/>
						</Item>
						<Item>
							<PoolName>BlendshapeStore</PoolName>
							<PoolSize value="150"/>
						</Item>
						<Item>
							<PoolName>Building</PoolName>
							<PoolSize value="75000"/>
						</Item>
						<Item>
							<!-- Size of CVehicleRecordingMgr's streaming module. -->
							<PoolName>carrec</PoolName>
							<PoolSize value="5500"/>
						</Item>
						<Item>
							<PoolName>CBoatChaseDirector</PoolName>
							<PoolSize value="8"/>
						</Item>
						<Item>
							<PoolName>CVehicleCombatAvoidanceArea</PoolName>
							<PoolSize value="5"/>
						</Item>
						<Item>
							<PoolName>CCargen</PoolName>
							<PoolSize value="8000"/>
						</Item>
						<Item>
							<PoolName>CCargenForScenarios</PoolName>
							<PoolSize value="5000"/>
						</Item>
						<Item>
							<PoolName>CCombatDirector</PoolName>
							<PoolSize value="50"/>
						</Item>
						<Item>
							<!-- RDE 4.0 requires a minimum of 19. -->
							<PoolName>CCombatInfo</PoolName>
							<PoolSize value="170"/>
						</Item>
						<Item>
							<PoolName>CCombatSituation</PoolName>
							<PoolSize value="60"/>
						</Item>
						<Item>
							<PoolName>CCoverFinder</PoolName>
							<PoolSize value="40"/>
						</Item>
						<Item>
							<PoolName>CDefaultCrimeInfo</PoolName>
							<PoolSize value="13"/>
						</Item>
						<Item>
							<PoolName>CTacticalAnalysis</PoolName>
							<PoolSize value="30"/>
						</Item>
						<Item>
							<PoolName>CTaskUseScenarioEntityExtension</PoolName>
							<PoolSize value="1024"/>
						</Item>
						<Item>
							<PoolName>AnimStore</PoolName>
							<PoolSize value="18500"/>
						</Item>
						<Item>
							<PoolName>CGameScriptResource</PoolName>
							<PoolSize value="5500"/>
						</Item>
						<Item>
							<PoolName>ClothStore</PoolName>
							<PoolSize value="60"/>
						</Item>
						<Item>
							<PoolName>CombatMeleeManager_Groups</PoolName>
							<PoolSize value="30"/>
						</Item>
						<Item>
							<PoolName>CombatMeleeManager_GroupsMP</PoolName>
							<PoolSize value="20"/>
						</Item>
						<Item>
							<PoolName>CombatMountedManager_Attacks</PoolName>
							<PoolSize value="1"/>
						</Item>
						<Item>
							<PoolName>CompEntity</PoolName>
							<PoolSize value="39"/>
						</Item>
						<Item>
							<PoolName>CPrioritizedClipSetBucket</PoolName>
							<PoolSize value="22"/>
						</Item>
						<Item>
							<PoolName>CPrioritizedClipSetRequest</PoolName>
							<PoolSize value="116"/>
						</Item>
						<Item>
							<PoolName>CRoadBlock</PoolName>
							<PoolSize value="36"/>
						</Item>
						<Item>
							<PoolName>CStuntJump</PoolName>
							<PoolSize value="64"/>
						</Item>
						<Item>
							<PoolName>CScenarioInfo</PoolName>
							<PoolSize value="880"/>
						</Item>
						<Item>
							<PoolName>CScenarioPointExtraData</PoolName>
							<PoolSize value="880"/>
						</Item>
						<Item>
							<PoolName>CutsceneStore</PoolName>
							<PoolSize value="1400"/>
						</Item>
						<Item>
							<PoolName>CScriptEntityExtension</PoolName>
							<PoolSize value="1400"/>
						</Item>
						<Item>
							<PoolName>CVehicleChaseDirector</PoolName>
							<PoolSize value="8"/>
						</Item>
						<Item>
							<PoolName>CVehicleClipRequestHelper</PoolName>
							<PoolSize value="45"/>
						</Item>
						<Item>
							<PoolName>CPathNodeRouteSearchHelper</PoolName>
							<PoolSize value="256"/>
						</Item>
						<Item>
							<PoolName>CGrabHelper</PoolName>
							<PoolSize value="8"/>
						</Item>
						<Item>
							<PoolName>CGpsNumNodesStored</PoolName>
							<PoolSize value="1024"/>
						</Item>
						<Item>
							<PoolName>CClimbHandHoldDetected</PoolName>
							<PoolSize value="32"/>
						</Item>
						<Item>
							<PoolName>CAmbientLookAt</PoolName>
							<PoolSize value="40"/>
						</Item>
						<Item>
							<PoolName>DecoratorExtension</PoolName>
							<PoolSize value="600"/>
						</Item>
						<Item>
							<PoolName>DrawableStore</PoolName>
							<PoolSize value="150200"/>
						</Item>
						<Item>
							<PoolName>Dummy Object</PoolName>
							<PoolSize value="15000"/>
						</Item>
						<Item>
							<PoolName>DwdStore</PoolName>
							<PoolSize value="150000"/>
						</Item>
						<Item>
							<PoolName>EntityBatch</PoolName>
							<PoolSize value="7500"/>
						</Item>
						<Item>
							<PoolName>GrassBatch</PoolName>
							<PoolSize value="30000"/>
						</Item>
						<Item>
							<PoolName>ExprDictStore</PoolName>
							<PoolSize value="600"/>
						</Item>
						<Item>
							<PoolName>FrameFilterStore</PoolName>
							<PoolSize value="14"/>
						</Item>
						<Item>
							<PoolName>FragmentStore</PoolName>
							<PoolSize value="250800"/>
						</Item>
						<Item>
							<PoolName>GamePlayerBroadcastDataHandler_Remote</PoolName>
							<PoolSize value="1550"/>
						</Item>
						<Item>
							<PoolName>InstanceBuffer</PoolName>
							<PoolSize value="20000"/>
						</Item>
						<Item>
							<PoolName>InteriorInst</PoolName>
							<PoolSize value="400"/>
						</Item>
						<Item>
							<PoolName>InteriorProxy</PoolName>
							<PoolSize value="1100"/>
						</Item>
						<Item>
							<PoolName>IplStore</PoolName>
							<PoolSize value="3000"/>
						</Item>
						<Item>
							<PoolName>MaxLoadedInfo</PoolName>
							<PoolSize value="46000"/>
						</Item>
						<Item>
							<PoolName>MaxLoadRequestedInfo</PoolName>
							<PoolSize value="24000"/>
						</Item>
						<Item>
							<PoolName>ActiveLoadedInfo</PoolName>
							<PoolSize value="24000"/>
						</Item>
						<Item>
							<PoolName>ActivePersistentLoadedInfo</PoolName>
							<PoolSize value="16000"/>
						</Item>
						<Item>
							<PoolName>Known Refs</PoolName>
							<PoolSize value="24000"/>
						</Item>
						<Item>
							<PoolName>LightEntity</PoolName>
							<PoolSize value="6000"/>
						</Item>
						<Item>
							<PoolName>MapDataLoadedNode</PoolName>
							<PoolSize value="5000"/>
						</Item>
						<Item>
							<PoolName>MapDataStore</PoolName>
							<PoolSize value="50000"/>
						</Item>
						<Item>
							<PoolName>MapTypesStore</PoolName>
							<PoolSize value="2800"/>
						</Item>
						<Item>
							<PoolName>MetaDataStore</PoolName>
							<PoolSize value="6000"/>
						</Item>
						<Item>
							<PoolName>NavMeshes</PoolName>
							<PoolSize value="17500"/>
						</Item>
						<Item>
							<PoolName>NetworkDefStore</PoolName>
							<PoolSize value="118"/>
						</Item>
						<Item>
							<PoolName>NetworkCrewDataMgr</PoolName>
							<PoolSize value="16"/>
						</Item>
						<Item>
							<PoolName>Object</PoolName>
							<!-- Raising this value can cause issues with recording -->
							<PoolSize value="2300"/>
						</Item>
						<Item>
							<PoolName>OcclusionInteriorInfo</PoolName>
							<PoolSize value="70"/>
						</Item>
						<Item>
							<PoolName>OcclusionPathNode</PoolName>
							<PoolSize value="5200"/>
						</Item>
						<Item>
							<PoolName>OcclusionPortalEntity</PoolName>
							<PoolSize value="250"/>
						</Item>
						<Item>
							<PoolName>OcclusionPortalInfo</PoolName>
							<PoolSize value="500"/>
						</Item>
						<Item>
							<PoolName>Peds</PoolName>
							<PoolSize value="256"/>
						</Item>
						<Item>
							<PoolName>CWeapon</PoolName>
							<PoolSize value="1024"/>
						</Item>
						<Item>
							<PoolName>phInstGta</PoolName>
							<PoolSize value="18000"/>
						</Item>
						<Item>
							<PoolName>PhysicsBounds</PoolName>
							<PoolSize value="1450"/>
						</Item>
						<Item>
							<PoolName>CPickup</PoolName>
							<PoolSize value="73"/>
						</Item>
						<Item>
							<PoolName>CPickupPlacement</PoolName>
							<PoolSize value="280"/>
						</Item>
						<Item>
							<PoolName>CPickupPlacementCustomScriptData</PoolName>
							<PoolSize value="200"/>
						</Item>
						<Item>
							<PoolName>CRegenerationInfo</PoolName>
							<PoolSize value="56"/>
						</Item>
						<Item>
							<PoolName>PortalInst</PoolName>
							<PoolSize value="600" />
						</Item>
						<Item>
							<PoolName>PoseMatcherStore</PoolName>
							<PoolSize value="28" />
						</Item>
						<Item>
							<PoolName>PMStore</PoolName>
							<PoolSize value="100"/>
						</Item>
						<Item>
							<PoolName>PtFxSortedEntity</PoolName>
							<PoolSize value="1000"/>
						</Item>
						<Item>
							<PoolName>PtFxAssetStore</PoolName>
							<PoolSize value="500"/>
						</Item>
						<Item>
							<PoolName>QuadTreeNodes</PoolName>
							<PoolSize value="1310"/>
						</Item>
						<Item>
							<PoolName>ScaleformStore</PoolName>
							<PoolSize value="700"/>
						</Item>
						<Item>
							<PoolName>ScaleformMgrArray</PoolName>
							<PoolSize value="40"/>
						</Item>
						<Item>
							<PoolName>ScriptStore</PoolName>
							<PoolSize value="920"/>
						</Item>
						<Item>
							<PoolName>StaticBounds</PoolName>
							<PoolSize value="45000"/>
						</Item>
						<Item>
							<PoolName>tcBox</PoolName>
							<PoolSize value="15000"/>
						</Item>
						<Item>
							<PoolName>TrafficLightInfos</PoolName>
							<PoolSize value="512"/>
						</Item>
						<Item>
							<PoolName>TxdStore</PoolName>
							<PoolSize value="200000"/>
						</Item>
						<Item>
							<PoolName>Vehicles</PoolName>
							<PoolSize value="300"/>
						</Item>
						<Item>
							<PoolName>VehicleStreamRequest</PoolName>
							<PoolSize value="240"/>
						</Item>
						<Item>
							<PoolName>VehicleStreamRender</PoolName>
							<PoolSize value="240"/>
						</Item>
						<Item>
							<PoolName>VehicleStruct</PoolName>
							<PoolSize value="600"/>
						</Item>
        					<Item>
							<PoolName>HandlingData</PoolName>
							<PoolSize value="5000"/>
						</Item>    
						<Item>
							<!-- Size of the CWaypointRecording streaming module. -->
							<PoolName>wptrec</PoolName>
							<PoolSize value="850"/>
						</Item>
						<Item>
							<PoolName>fwLodNode</PoolName>
							<PoolSize value="25000"/>
						</Item>
						<Item>
							<PoolName>CTask</PoolName>
							<PoolSize value="8192"/>
						</Item>
						<Item>
						<!-- Increasing this value in addition to ctasksequencelist can resolve GTA.Native.?A0x55605b1d.NativeTask.Run() crashes in wineventlog -->
							<PoolName>CEvent</PoolName>
							<PoolSize value="4000"/>
						</Item>
						<Item>
							<PoolName>CMoveObject</PoolName>
							<PoolSize value="500"/>
						</Item>
						<Item>
							<PoolName>CMoveAnimatedBuilding</PoolName>
							<PoolSize value="500"/>
						</Item>
						<Item>
							<PoolName>atDScriptObjectNode</PoolName>
							<PoolSize value="1400"/>
						</Item>
						<Item>
							<PoolName>fwDynamicArchetypeComponent</PoolName>
							<PoolSize value="50000"/>
						</Item>
						<Item>
							<PoolName>fwDynamicEntityComponent</PoolName>
							<PoolSize value="40000"/>
						</Item>
						<Item>
							<PoolName>fwEntityContainer</PoolName>
							<PoolSize value="1250"/>
						</Item>
						<Item>
							<PoolName>fwMatrixTransform</PoolName>
							<PoolSize value="90000"/>
						</Item>
						<Item>
							<PoolName>fwQuaternionTransform</PoolName>
							<PoolSize value="38874"/>
						</Item>
						<Item>
							<PoolName>fwSimpleTransform</PoolName>
							<PoolSize value="111000"/>
						</Item>
						<Item>
							<PoolName>ScenarioCarGensPerRegion</PoolName>
							<PoolSize value="320"/>
						</Item>
						<Item>
							<PoolName>ScenarioPointsAndEdgesPerRegion</PoolName>
							<PoolSize value="2000"/>
						</Item>
						<Item>
							<PoolName>ScenarioPoint</PoolName>
							<PoolSize value="1800"/>
						</Item>
						<Item>
							<PoolName>ScenarioPointEntity</PoolName>
							<PoolSize value="700"/>
						</Item>
						<Item>
							<PoolName>ScenarioPointWorld</PoolName>
							<PoolSize value="2800"/>
						</Item>
						<Item>
							<PoolName>MaxNonRegionScenarioPointSpatialObjects</PoolName>
							<PoolSize value="1800"/>
						</Item>
						<Item>
							<PoolName>ObjectIntelligence</PoolName>
							<PoolSize value="120"/>
						</Item>
						<Item>
							<PoolName>VehicleScenarioAttractors</PoolName>
							<PoolSize value="64"/>
						</Item>
						<Item>
							<PoolName>AircraftFlames</PoolName>
							<PoolSize value="34"/>
						</Item>
						<Item>
							<PoolName>CScenarioPointChainUseInfo</PoolName>
							<PoolSize value="96"/>
						</Item>
						<Item>
							<PoolName>CScenarioClusterSpawnedTrackingData</PoolName>
							<PoolSize value="190"/>
						</Item>
						<Item>
							<PoolName>CSPClusterFSMWrapper</PoolName>
							<PoolSize value="192"/>
						</Item>
						<Item>
							<PoolName>fwArchetypePooledMap</PoolName>
							<PoolSize value="128000"/>
						</Item>
						<Item>
							<PoolName>CTaskConversationHelper</PoolName>
							<PoolSize value="4"/>
						</Item>
						<Item>
							<PoolName>SyncedScenes</PoolName>
							<PoolSize value="50"/>
						</Item>
						<Item>
							<PoolName>AnimScenes</PoolName>
							<PoolSize value="10"/>
						</Item>
						<Item>
							<PoolName>CPropManagementHelper</PoolName>
							<PoolSize value="256"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Definitions</PoolName>
							<PoolSize value="306"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Results</PoolName>
							<PoolSize value="474"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Impulses</PoolName>
							<PoolSize value="20"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Interrelations</PoolName>
							<PoolSize value="60"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Homings</PoolName>
							<PoolSize value="167"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Damages</PoolName>
							<PoolSize value="24"/>
						</Item>
						<Item>
							<PoolName>ActionTable_StrikeBones</PoolName>
							<PoolSize value="18"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Rumbles</PoolName>
							<PoolSize value="5"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Branches</PoolName>
							<PoolSize value="27"/>
						</Item>
						<Item>
							<PoolName>ActionTable_StealthKills</PoolName>
							<PoolSize value="10"/>
						</Item>
						<Item>
							<PoolName>ActionTable_Vfx</PoolName>
							<PoolSize value="35"/>
						</Item>
						<Item>
							<PoolName>ActionTable_FacialAnimSets</PoolName>
							<PoolSize value="5"/>
						</Item>
						<Item>
							<PoolName>NetworkEntityAreas</PoolName>
							<PoolSize value="200"/>
						</Item>
						<Item>
							<PoolName>NavMeshRoute</PoolName>
							<PoolSize value="1024"/>
						</Item>
					</Entries>
				</PoolSizes>

				<ConfigPopulation>
					<ScenarioPedsMultiplier_Base value="70"/>
					<ScenarioPedsMultiplier value="100"/>
					<AmbientPedsMultiplier_Base value="70"/>
					<AmbientPedsMultiplier value="100"/>
					<MaxTotalPeds_Base value="70"/>
					<MaxTotalPeds value="200"/>
					<PedMemoryMultiplier value="500"/>
					<PedsForVehicles_Base value="75"/>
					<PedsForVehicles value="75"/>
					<VehicleTimesliceMaxUpdatesPerFrame_Base value="4"/>
					<VehicleTimesliceMaxUpdatesPerFrame value="10"/>
					<VehicleAmbientDensityMultiplier_Base value="66"/>
					<VehicleAmbientDensityMultiplier value="100"/>
					<VehicleMemoryMultiplier value="500"/>
					<VehicleParkedDensityMultiplier_Base value="50"/>
					<VehicleParkedDensityMultiplier value="130"/>
					<VehicleLowPrioParkedDensityMultiplier_Base value="50"/>
					<VehicleLowPrioParkedDensityMultiplier value="130"/>
					<VehicleUpperLimit_Base value="50"/>
					<VehicleUpperLimit value="130"/>
					<VehicleUpperLimitMP value="60"/>
					<VehicleParkedUpperLimit_Base value="50"/>
					<VehicleParkedUpperLimit value="130"/>
					<VehicleKeyholeShapeInnerThickness_Base value="20"/>
					<VehicleKeyholeShapeInnerThickness value="20"/>
					<VehicleKeyholeShapeOuterThickness_Base value="40"/>
					<VehicleKeyholeShapeOuterThickness value="40"/>
					<VehicleKeyholeShapeInnerRadius_Base value="80"/>
					<VehicleKeyholeShapeInnerRadius value="120"/>
					<VehicleKeyholeShapeOuterRadius_Base value="185"/>
					<VehicleKeyholeShapeOuterRadius value="215"/>
					<VehicleKeyholeSideWallThickness_Base value="60"/>
					<VehicleKeyholeSideWallThickness value="60"/>
					<VehicleMaxCreationDistance_Base value="225"/>
					<VehicleMaxCreationDistance value="255"/>
					<VehicleMaxCreationDistanceOffscreen_Base value="50"/>
					<VehicleMaxCreationDistanceOffscreen value="50"/>
					<VehicleCullRange_Base value="251"/>
					<VehicleCullRange value="311"/>
					<VehicleCullRangeOnScreenScale_Base value="140"/>
					<VehicleCullRangeOnScreenScale value="140"/>
					<VehicleCullRangeOffScreen_Base value="100"/>
					<VehicleCullRangeOffScreen value="150"/>
					<DensityBasedRemovalRateScale_Base value="36"/>
					<DensityBasedRemovalRateScale value="36"/>
					<DensityBasedRemovalTargetHeadroom_Base value="10"/>
					<DensityBasedRemovalTargetHeadroom value="10"/>
					<VehicleSpacing_Base>
						<VehicleSpacing_0_Base value="1"/>
						<VehicleSpacing_1_Base value="172"/>
						<VehicleSpacing_2_Base value="150"/>
						<VehicleSpacing_3_Base value="129"/>
						<VehicleSpacing_4_Base value="110"/>
						<VehicleSpacing_5_Base value="88"/>
						<VehicleSpacing_6_Base value="55"/>
						<VehicleSpacing_7_Base value="52"/>
						<VehicleSpacing_8_Base value="45"/>
						<VehicleSpacing_9_Base value="40"/>
						<VehicleSpacing_10_Base value="34"/>
						<VehicleSpacing_11_Base value="27"/>
						<VehicleSpacing_12_Base value="22"/>
						<VehicleSpacing_13_Base value="20"/>
						<VehicleSpacing_14_Base value="19"/>
						<VehicleSpacing_15_Base value="18"/>
					</VehicleSpacing_Base>
					<VehicleSpacing>
						<VehicleSpacing_0 value="1"/>
						<VehicleSpacing_1 value="172"/>
						<VehicleSpacing_2 value="150"/>
						<VehicleSpacing_3 value="129"/>
						<VehicleSpacing_4 value="110"/>
						<VehicleSpacing_5 value="88"/>
						<VehicleSpacing_6 value="55"/>
						<VehicleSpacing_7 value="52"/>
						<VehicleSpacing_8 value="45"/>
						<VehicleSpacing_9 value="40"/>
						<VehicleSpacing_10 value="34"/>
						<VehicleSpacing_11 value="27"/>
						<VehicleSpacing_12 value="22"/>
						<VehicleSpacing_13 value="20"/>
						<VehicleSpacing_14 value="19"/>
						<VehicleSpacing_15 value="18"/>
					</VehicleSpacing>
					<PlayersRoadScanDistance_Base value="300"/>
					<PlayersRoadScanDistance value="330"/>
					<PlayerRoadDensityInc_Base>
						<PlayerRoadDensityInc_0_Base value="0"/>
						<PlayerRoadDensityInc_1_Base value="0"/>
						<PlayerRoadDensityInc_2_Base value="0"/>
						<PlayerRoadDensityInc_3_Base value="0"/>
						<PlayerRoadDensityInc_4_Base value="0"/>
						<PlayerRoadDensityInc_5_Base value="0"/>
						<PlayerRoadDensityInc_6_Base value="0"/>
						<PlayerRoadDensityInc_7_Base value="0"/>
						<PlayerRoadDensityInc_8_Base value="0"/>
						<PlayerRoadDensityInc_9_Base value="0"/>
						<PlayerRoadDensityInc_10_Base value="0"/>
						<PlayerRoadDensityInc_11_Base value="0"/>
						<PlayerRoadDensityInc_12_Base value="0"/>
						<PlayerRoadDensityInc_13_Base value="0"/>
						<PlayerRoadDensityInc_14_Base value="0"/>
						<PlayerRoadDensityInc_15_Base value="0"/>
					</PlayerRoadDensityInc_Base>
					<PlayerRoadDensityInc>
						<PlayerRoadDensityInc_0 value="0"/>
						<PlayerRoadDensityInc_1 value="0"/>
						<PlayerRoadDensityInc_2 value="0"/>
						<PlayerRoadDensityInc_3 value="0"/>
						<PlayerRoadDensityInc_4 value="0"/>
						<PlayerRoadDensityInc_5 value="0"/>
						<PlayerRoadDensityInc_6 value="2"/>
						<PlayerRoadDensityInc_7 value="2"/>
						<PlayerRoadDensityInc_8 value="2"/>
						<PlayerRoadDensityInc_9 value="2"/>
						<PlayerRoadDensityInc_10 value="2"/>
						<PlayerRoadDensityInc_11 value="1"/>
						<PlayerRoadDensityInc_12 value="0"/>
						<PlayerRoadDensityInc_13 value="0"/>
						<PlayerRoadDensityInc_14 value="0"/>
						<PlayerRoadDensityInc_15 value="0"/>
					</PlayerRoadDensityInc>
					<NonPlayerRoadDensityDec_Base>
						<NonPlayerRoadDensityDec_0_Base value="0"/>
						<NonPlayerRoadDensityDec_1_Base value="0"/>
						<NonPlayerRoadDensityDec_2_Base value="0"/>
						<NonPlayerRoadDensityDec_3_Base value="1"/>
						<NonPlayerRoadDensityDec_4_Base value="1"/>
						<NonPlayerRoadDensityDec_5_Base value="1"/>
						<NonPlayerRoadDensityDec_6_Base value="1"/>
						<NonPlayerRoadDensityDec_7_Base value="2"/>
						<NonPlayerRoadDensityDec_8_Base value="2"/>
						<NonPlayerRoadDensityDec_9_Base value="2"/>
						<NonPlayerRoadDensityDec_10_Base value="2"/>
						<NonPlayerRoadDensityDec_11_Base value="2"/>
						<NonPlayerRoadDensityDec_12_Base value="3"/>
						<NonPlayerRoadDensityDec_13_Base value="3"/>
						<NonPlayerRoadDensityDec_14_Base value="3"/>
						<NonPlayerRoadDensityDec_15_Base value="3"/>
					</NonPlayerRoadDensityDec_Base>
					<NonPlayerRoadDensityDec>
						<NonPlayerRoadDensityDec_0 value="0"/>
						<NonPlayerRoadDensityDec_1 value="0"/>
						<NonPlayerRoadDensityDec_2 value="0"/>
						<NonPlayerRoadDensityDec_3 value="0"/>
						<NonPlayerRoadDensityDec_4 value="0"/>
						<NonPlayerRoadDensityDec_5 value="0"/>
						<NonPlayerRoadDensityDec_6 value="0"/>
						<NonPlayerRoadDensityDec_7 value="0"/>
						<NonPlayerRoadDensityDec_8 value="0"/>
						<NonPlayerRoadDensityDec_9 value="0"/>
						<NonPlayerRoadDensityDec_10 value="0"/>
						<NonPlayerRoadDensityDec_11 value="1"/>
						<NonPlayerRoadDensityDec_12 value="2"/>
						<NonPlayerRoadDensityDec_13 value="3"/>
						<NonPlayerRoadDensityDec_14 value="4"/>
						<NonPlayerRoadDensityDec_15 value="5"/>
					</NonPlayerRoadDensityDec>
					<VehiclePopulationFrameRate_Base value="20"/>
					<VehiclePopulationFrameRate value="25"/>
					<VehiclePopulationCyclesPerFrame_Base value="1"/>
					<VehiclePopulationCyclesPerFrame value="1"/>
					<VehiclePopulationFrameRateMP_Base value="15"/>
					<VehiclePopulationFrameRateMP value="20"/>
					<VehiclePopulationCyclesPerFrameMP_Base value="1"/>
					<VehiclePopulationCyclesPerFrameMP value="1"/>
					<PedPopulationFrameRate_Base value="20"/>
					<PedPopulationFrameRate value="25"/>
					<PedPopulationCyclesPerFrame_Base value="1"/>
					<PedPopulationCyclesPerFrame value="1"/>
					<PedPopulationFrameRateMP_Base value="15"/>
					<PedPopulationFrameRateMP value="20"/>
					<PedPopulationCyclesPerFrameMP_Base value="1"/>
					<PedPopulationCyclesPerFrameMP value="1"/>
				</ConfigPopulation>

				<Config2dEffects>
					<MaxAttrsAudio value="280"/>
					<MaxAttrsBuoyancy value="100"/>
					<MaxAttrsDecal value="200"/>
					<MaxAttrsExplosion value="200"/>
					<MaxAttrsLadder value="122"/>
					<MaxAttrsLightShaft value="1000"/>
					<MaxAttrsParticle value="5000"/>
					<MaxAttrsProcObj value="200"/>
					<MaxAttrsScrollBar value="1"/>
					<MaxAttrsSpawnPoint value="1000"/>
					<MaxAttrsWindDisturbance value="100"/>
					<MaxAttrsWorldPoint value="1000"/>
					<MaxEffectsWorld2d value="1000"/>
					<!-- R* cap = 0 <MaxClothCollisionsExtensions value="0"/> : Doesn't appear to be used-->
				</Config2dEffects>

				<ConfigModelInfo>
					<defaultPlayerName>player_zero</defaultPlayerName>
					<defaultProloguePlayerName>csb_prolsec</defaultProloguePlayerName>
					<MaxBaseModelInfos value="2"/>
					<MaxCompEntityModelInfos value="500"/>
					<MaxMloInstances value="28000"/>
					<MaxMloModelInfos value="5000"/>
					<MaxPedModelInfos value="5000"/>
					<MaxTimeModelInfos value="1800"/>
					<MaxVehicleModelInfos value="5000"/>
					<MaxWeaponModelInfos value="5000"/>
					<MaxExtraPedModelInfos value="5000"/>
					<MaxExtraVehicleModelInfos value="5010"/>
					<MaxExtraWeaponModelInfos value="5000"/>
				</ConfigModelInfo>

				<ConfigExtensions>
					<MaxDoorExtensions value="64"/>
					<MaxLightExtensions value="1024"/>
					<MaxSpawnPointOverrideExtensions value="255"/>
					<MaxExpressionExtensions value="255"/>
				</ConfigExtensions>

				<ConfigStreamingEngine>
					<ArchiveCount value="4772"/>
					<PhysicalStreamingBuffer value="252"/>
					<VirtualStreamingBuffer value="1000"/>
				</ConfigStreamingEngine>

				<UseVehicleBurnoutTexture>CB_TRUE</UseVehicleBurnoutTexture>
				<AllowCrouchedMovement>CB_FALSE</AllowCrouchedMovement>
				<AllowParachuting>CB_TRUE</AllowParachuting>
				<AllowStealthMovement>CB_TRUE</AllowStealthMovement>
				<DebugScriptsPath>x:\gta5\script\dev\singleplayer\sco\DEBUG\</DebugScriptsPath>

				<Threads>
					<Item key="Streamer">
						<Priority>PRIO_NORMAL</Priority>
					</Item>
					<Item key="Update">
						<Priority>PRIO_NORMAL</Priority>
					</Item>
					<Item key="Render">
						<Priority>PRIO_NORMAL</Priority>
					</Item>
					<Item key="PathServer">
						<Priority>PRIO_LOWEST</Priority>
					</Item>
					<Item key="SysTask">
						<Priority>PRIO_ABOVE_NORMAL</Priority>
					</Item>
					<Item key="ControlMgrUpdateThread">
						<Priority>PRIO_ABOVE_NORMAL</Priority>
					</Item>
				</Threads>

				<ConfigOnlineServices>
					<RosTitleName>gta5</RosTitleName>
					<RosTitleVersion value="11"/>
					<RosScVersion value="11"/>
					<SteamAppId value="271590"/>
					<TitleDirectoryName>GTA V</TitleDirectoryName>
					<MultiplayerSessionTemplateName>SsnTemplateOpen</MultiplayerSessionTemplateName>
					<ScAuthTitleId>gtav</ScAuthTitleId>
				</ConfigOnlineServices>

				<ConfigUGCDescriptions>
					<MaxDescriptionLength value="255"/>
					<MaxNumDescriptions value="640"/>
					<SizeOfDescriptionBuffer value="60000"/>
				</ConfigUGCDescriptions>

				<ConfigNetScriptBroadcastData>
					<HostBroadcastData>
						<Item>
							<SizeOfData value="14000"/>
							<MaxParticipants value="32"/>
							<NumInstances value="5"/>
						</Item>
						<Item>
							<SizeOfData value="6500"/>
							<MaxParticipants value="32"/>
							<NumInstances value="6"/>
						</Item>
						<Item>
							<SizeOfData value="4000"/>
							<MaxParticipants value="32"/>
							<NumInstances value="6"/>
						</Item>
						<Item>
							<SizeOfData value="2000"/>
							<MaxParticipants value="32"/>
							<NumInstances value="2"/>
						</Item>
						<Item>
							<SizeOfData value="1500"/>
							<MaxParticipants value="32"/>
							<NumInstances value="4"/>
						</Item>
						<Item>
							<SizeOfData value="1000"/>
							<MaxParticipants value="32"/>
							<NumInstances value="10"/>
						</Item>
						<Item>
							<SizeOfData value="500"/>
							<MaxParticipants value="32"/>
							<NumInstances value="4"/>
						</Item>
						<Item>
							<SizeOfData value="250"/>
							<MaxParticipants value="32"/>
							<NumInstances value="4"/>
						</Item>
						<Item>
							<SizeOfData value="120"/>
							<MaxParticipants value="32"/>
							<NumInstances value="6"/>
						</Item>
						<Item>
							<SizeOfData value="60"/>
							<MaxParticipants value="32"/>
							<NumInstances value="6"/>
						</Item>
					</HostBroadcastData>
					<PlayerBroadcastData>
						<Item>
							<SizeOfData value="3600"/>
							<MaxParticipants value="32"/>
							<NumInstances value="1"/>
						</Item>
						<Item>
							<SizeOfData value="2500"/>
							<MaxParticipants value="32"/>
							<NumInstances value="2"/>
						</Item>
						<Item>
							<SizeOfData value="1400"/>
							<MaxParticipants value="32"/>
							<NumInstances value="4"/>
						</Item>
						<Item>
							<SizeOfData value="600"/>
							<MaxParticipants value="32"/>
							<NumInstances value="2"/>
						</Item>
						<Item>
							<SizeOfData value="500"/>
							<MaxParticipants value="32"/>
							<NumInstances value="3"/>
						</Item>
						<Item>
							<SizeOfData value="400"/>
							<MaxParticipants value="32"/>
							<NumInstances value="4"/>
						</Item>
						<Item>
							<SizeOfData value="150"/>
							<MaxParticipants value="32"/>
							<NumInstances value="2"/>
						</Item>
						<Item>
							<SizeOfData value="80"/>
							<MaxParticipants value="32"/>
							<NumInstances value="4"/>
						</Item>
						<Item>
							<SizeOfData value="40"/>
							<MaxParticipants value="32"/>
							<NumInstances value="8"/>
						</Item>
						<Item>
							<SizeOfData value="16"/>
							<MaxParticipants value="32"/>
							<NumInstances value="16"/>
						</Item>
					</PlayerBroadcastData>
				</ConfigNetScriptBroadcastData>

				<ConfigScriptStackSizes>
					<StackSizeData>
						<Item>
							<StackName>MICRO</StackName>
							<SizeOfStack value="128"/>
							<NumberOfStacksOfThisSize value="20"/>
						</Item>
						<Item>
							<StackName>MINI</StackName>
							<SizeOfStack value="512"/>
							<NumberOfStacksOfThisSize value="20"/>
						</Item>
						<Item>
							<StackName>DEFAULT</StackName>
							<SizeOfStack value="1424"/> 
							<NumberOfStacksOfThisSize value="68"/>
						</Item>
						<Item>
							<StackName>SPECIAL_ABILITY</StackName>
							<SizeOfStack value="1828"/>
							<NumberOfStacksOfThisSize value="13"/>
						</Item>
						<Item>
							<StackName>FRIEND</StackName>
							<SizeOfStack value="2050"/>
							<NumberOfStacksOfThisSize value="12"/>
						</Item>
						<Item>
							<StackName>SHOP</StackName>
							<SizeOfStack value="2324"/>
							<NumberOfStacksOfThisSize value="6"/>
						</Item>
						<Item>
							<StackName>CELLPHONE</StackName>
							<SizeOfStack value="2552"/>
							<NumberOfStacksOfThisSize value="2"/>
						</Item>
						<Item>
							<StackName>VEHICLE_SPAWN</StackName>
							<SizeOfStack value="3668"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>CAR_MOD_SHOP</StackName>
							<SizeOfStack value="3472"/>
							<NumberOfStacksOfThisSize value="2"/>
						</Item>
						<Item>
							<StackName>PAUSE_MENU_SCRIPT</StackName>
							<SizeOfStack value="3076"/>
							<NumberOfStacksOfThisSize value="2"/>
						</Item>
						<Item>
						  <StackName>APP_INTERNET</StackName>
						  <SizeOfStack value="4592"/>
						  <NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>MULTIPLAYER_MISSION</StackName>
							<SizeOfStack value="4500"/>
							<NumberOfStacksOfThisSize value="19"/>
						</Item>
						<Item>
							<StackName>CONTACTS_APP</StackName>
							<SizeOfStack value="4000"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
						  <StackName>INTERACTION_MENU</StackName>
						  <SizeOfStack value="9800"/>
						  <NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>SCRIPT_XML</StackName>
							<SizeOfStack value="8500"/>
							<NumberOfStacksOfThisSize value="4"/>
						</Item>
						<Item>
							<StackName>PROPERTY_INT</StackName>
							<SizeOfStack value="19400"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>ACTIVITY_CREATOR_INT</StackName>
							<SizeOfStack value="15400"/>
							<NumberOfStacksOfThisSize value="3"/>
						</Item>
						<Item>
							<StackName>SMPL_INTERIOR</StackName>
							<SizeOfStack value="6000"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>WAREHOUSE</StackName>
							<SizeOfStack value="14000"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>IE_DELIVERY</StackName>
							<SizeOfStack value="2024"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>SHOP_CONTROLLER</StackName>
							<SizeOfStack value="2456"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>AM_MP_YACHT</StackName>
							<SizeOfStack value="5000"/>
							<NumberOfStacksOfThisSize value="3"/>
						</Item>
						<Item>
							<StackName>INGAMEHUD</StackName>
							<SizeOfStack value="4600"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>TRANSITION</StackName>
							<SizeOfStack value="8032"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>FMMC_LAUNCHER</StackName>
                            <SizeOfStack value="17000"/>
                            <NumberOfStacksOfThisSize value="1"/>
                        </Item>
                        <Item>
                            <StackName>MULTIPLAYER_FREEMODE</StackName>
                            <SizeOfStack value="57250"/>
                            <NumberOfStacksOfThisSize value="1"/>
                        </Item>
                        <Item>
                            <StackName>MISSION</StackName>
                            <SizeOfStack value="28000"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>MP_LAUNCH_SCRIPT</StackName>
							<SizeOfStack value="24490"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						
						
					</StackSizeData>
				</ConfigScriptStackSizes>

				<ConfigScriptTextLines>
					<ArrayOfMaximumTextLines>
						<Item>
							<NameOfScriptTextLine>ScriptTextLinesZeroOrOneNumbers</NameOfScriptTextLine>
							<MaximumNumber value="160"/>
						</Item>
						<Item>
							<NameOfScriptTextLine>ScriptTextLinesOneSubstring</NameOfScriptTextLine>
							<MaximumNumber value="144"/>
						</Item>
						<Item>
							<NameOfScriptTextLine>ScriptTextLinesFourSubstringsThreeNumbers</NameOfScriptTextLine>
							<MaximumNumber value="25"/>
						</Item>
					</ArrayOfMaximumTextLines>
				</ConfigScriptTextLines>

			</Config>
		</Item>

		<!-- Debug configuration overrides -->
		<Item>
			<Build>debug</Build>
			<Platforms>Any</Platforms>
			<Config type="CGameConfig">
				<ConfigStreamingEngine>
					<PhysicalStreamingBuffer value="252"/>
				</ConfigStreamingEngine>
			</Config>
		</Item>
		
		<!-- Beta configuration overrides -->
		<Item>
			<Build>beta</Build>
			<Platforms>Any</Platforms>
			<Config type="CGameConfig">
				<PoolSizes>
					<Entries>
						<!-- test_startup creates lots of peds and cars around Pershing Square -->
						<Item>
							<PoolName>CScriptEntityExtension</PoolName>
							<PoolSize value="700"/>
						</Item>
					</Entries>
				</PoolSizes>
				<ConfigStreamingEngine>
					<PhysicalStreamingBuffer value="252"/>
				</ConfigStreamingEngine>
			</Config>
		</Item>

		<!-- Nonfinal param configuration overrides -->
		<Item>
			<Build>nonfinal</Build>
			<Platforms>Any</Platforms>
			<Param>usefatcuts</Param>
			<Config type="CGameConfig">
				<PoolSizes>
					<Entries>
						<!-- fatcuts needs a bigger animation pool -->
							<Item>
								<PoolName>AnimStore</PoolName>
								<PoolSize value="15000"/>
							</Item>
							<Item>
								<PoolName>CutSceneStore</PoolName>
								<PoolSize value="15000"/>
							</Item>
					</Entries>
				</PoolSizes>
			</Config>
		</Item>

    <Item>
			<Build>any</Build>
			<Platforms>xboxone</Platforms>
			<Config type="CGameConfig">
			<PoolSizes>
				<Entries>
					<Item>
						<PoolName>OcclusionPathNode</PoolName>	
						<PoolSize value="3450"/>
					</Item>
					<Item>
						<PoolName>OcclusionPortalInfo</PoolName>
						<PoolSize value="400"/>
					</Item>
				</Entries>
			</PoolSizes>
				<ConfigStreamingEngine>
					<PhysicalStreamingBuffer value="2384"/>
					<VirtualStreamingBuffer value="0"/>
				</ConfigStreamingEngine>
        <ConfigMediaTranscoding>
          <TranscodingSmallObjectBuffer value="4096"/>
          <TranscodingSmallObjectMaxPointers value="6144"/>
          <TranscodingBuffer value="24000"/>
          <TranscodingMaxPointers value="256"/>
        </ConfigMediaTranscoding>
        <Threads>
          <Item key="Update">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="0"/>
			</CpuAffinity>
          </Item>
          <Item key="AsyncShapeTestMgr">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RmptfxUpdateThread">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="ControlMgrUpdateThread">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadDefault">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="ReplayQuantizeThread">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadGameAndObject">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="MediaEncoderThreadAudio">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RageDvdReader">
            <Priority>PRIO_TIME_CRITICAL</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="RageHddReader">
            <Priority>PRIO_TIME_CRITICAL</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="RecorderWorkerThread">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadPed">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="PathServer">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="Render">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="NetLogSpooler">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="NetRelay">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="RageLogfile">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="RageNetTcpWorker">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="RageAudioMixThread">
            <Priority>PRIO_TIME_CRITICAL</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="RageAudioEngineThread">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="SaveBlockDataThread">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="RageDvdStreamer">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="RageHddStreamer">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadVehicle">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="NorthAudioUpdate">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="RageNetSend">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="RageNetRecv">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="RageVoiceChatWorker">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="MediaEncoderThreadVideo">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="MediaDecoderThread">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="ReplayFileManager">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="ResourcePlacementThread">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
        </Threads>
			</Config>
		</Item>

    <Item>
			<Build>any</Build>
			<Platforms>ps4</Platforms>
      <Config type="CGameConfig">
				<PoolSizes>
          <Entries>
            <Item>
              <PoolName>CTask</PoolName>
              <PoolSize value="2100"/>
            </Item>
			<Item>
				<PoolName>OcclusionPathNode</PoolName>
				<PoolSize value="3450"/>
			</Item>
			<Item>
				<PoolName>OcclusionPortalInfo</PoolName>
				<PoolSize value="400"/>
			</Item>
          </Entries>
        </PoolSizes>
				<ConfigStreamingEngine>
					<PhysicalStreamingBuffer value="2384"/>
					<VirtualStreamingBuffer value="0"/>
				</ConfigStreamingEngine>
        <Threads>
          <Item key="Update">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="0"/>
			</CpuAffinity>
          </Item>
          <Item key="ControlMgrUpdateThread">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="AsyncShapeTestMgr">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RageDvdReader">
            <Priority>PRIO_TIME_CRITICAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadDefault">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="ReplayQuantizeThread">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadGameAndObject">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
		  <Item key="MediaEncoderThreadAudio">
            <Priority>PRIO_LOWEST</Priority>
			<CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="RageAudioEngineThread">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RageHddReader">
            <Priority>PRIO_TIME_CRITICAL</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="RmptfxUpdateThread">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadPed">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="PathServer">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="2"/>
			</CpuAffinity>
          </Item>
          <Item key="RageGpuSubmit">
            <Priority>PRIO_TIME_CRITICAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="RecordingThreadVehicle">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="NetLogSpooler">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="NetRelay">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="RageLogfile">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="RageNetTcpWorker">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="ResourcePlacementThread">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="3"/>
			</CpuAffinity>
          </Item>
          <Item key="RageAudioMixThread">
            <Priority>PRIO_TIME_CRITICAL</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="SaveBlockDataThread">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="RageDvdStreamer">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="RageHddStreamer">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="4"/>
			</CpuAffinity>
          </Item>
          <Item key="Render">
            <Priority>PRIO_HIGHEST</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="NorthAudioUpdate">
            <Priority>PRIO_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="RageNetSend">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="RageNetRecv">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="RageVoiceChatWorker">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
		  <Item key="MediaEncoderThreadVideo">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
          <Item key="ReplayFileManager">
            <Priority>PRIO_LOWEST</Priority>
            <CpuAffinity>
                <Core value="5"/>
			</CpuAffinity>
          </Item>
        </Threads>
			</Config>
		</Item>
    <Item>
      <Build>Debug</Build>
			<Platforms>ps4</Platforms>
			<Config type="CGameConfig">
        <Threads>
          <Item key="RageNetSend">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RageNetRecv">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="RageVoiceChatWorker">
            <Priority>PRIO_BELOW_NORMAL</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
          <Item key="PathServer">
            <Priority>PRIO_IDLE</Priority>
            <CpuAffinity>
                <Core value="1"/>
			</CpuAffinity>
          </Item>
        </Threads>
			</Config>
		</Item>

    <Item>
      <Build>any</Build>
      <Platforms>x64</Platforms>
      <Config type="CGameConfig">
        <Threads>
          <Item key="Update">
            <Priority>PRIO_TIME_CRITICAL</Priority>
          </Item>
          <Item key="ControlMgrUpdateThread">
            <Priority>PRIO_HIGHEST</Priority>
          </Item>
          <Item key="AsyncShapeTestMgr">
            <Priority>PRIO_HIGHEST</Priority>
          </Item>
          <Item key="RageDvdReader">
            <Priority>PRIO_TIME_CRITICAL</Priority>
          </Item>
          <Item key="RecordingThreadDefault">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
          </Item>
          <Item key="ReplayQuantizeThread">
            <Priority>PRIO_BELOW_NORMAL</Priority>
          </Item>
          <Item key="RecordingThreadGameAndObject">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
          </Item>
          <Item key="RageAudioEngineThread">
            <Priority>PRIO_NORMAL</Priority>
          </Item>
          <Item key="RageHddReader">
            <Priority>PRIO_TIME_CRITICAL</Priority>
          </Item>
          <Item key="RmptfxUpdateThread">
            <Priority>PRIO_HIGHEST</Priority>
          </Item>
          <Item key="RecordingThreadPed">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
          </Item>
          <Item key="PathServer">
            <Priority>PRIO_LOWEST</Priority>
          </Item>
          <Item key="RecordingThreadVehicle">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
          </Item>
          <Item key="ResourcePlacementThread">
            <Priority>PRIO_LOWEST</Priority>
          </Item>
          <Item key="RageAudioMixThread">
            <Priority>PRIO_TIME_CRITICAL</Priority>
          </Item>
          <Item key="SaveBlockDataThread">
            <Priority>PRIO_NORMAL</Priority>
          </Item>
          <Item key="RageDvdStreamer">
            <Priority>PRIO_BELOW_NORMAL</Priority>
          </Item>
          <Item key="RageHddStreamer">
            <Priority>PRIO_LOWEST</Priority>
          </Item>
          <Item key="Render">
            <Priority>PRIO_ABOVE_NORMAL</Priority>
          </Item>
          <Item key="NorthAudioUpdate">
            <Priority>PRIO_NORMAL</Priority>
          </Item>
          <Item key="RageNetSend">
            <Priority>PRIO_BELOW_NORMAL</Priority>
          </Item>
          <Item key="RageNetRecv">
            <Priority>PRIO_BELOW_NORMAL</Priority>
          </Item>
          <Item key="RageVoiceChatWorker">
            <Priority>PRIO_BELOW_NORMAL</Priority>
          </Item>
          <Item key="ReplayFileManager">
            <Priority>PRIO_LOWEST</Priority>
          </Item>
        </Threads>
      </Config>
    </Item>
		<Item>
			<Build>nonfinal</Build>
			<Platforms>any</Platforms>
			<Config type="CGameConfig">
				<ConfigScriptStackSizes>
					<StackSizeData>
						<Item>
							<StackName>DEBUG_SCRIPT</StackName>
							<SizeOfStack value="4080"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>SOAK_TEST</StackName>
							<SizeOfStack value="4088"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
						<Item>
							<StackName>NETWORK_BOT</StackName>
							<SizeOfStack value="4096"/>
							<NumberOfStacksOfThisSize value="31"/>
						</Item>
						<Item>
							<StackName>DEBUG_MENU</StackName>
							<SizeOfStack value="32000"/>
							<NumberOfStacksOfThisSize value="1"/>
						</Item>
					</StackSizeData>
				</ConfigScriptStackSizes>
			</Config>
		</Item>

		<Item>
			<Build>nonfinal</Build>
			<Platforms>any</Platforms>
			<Config type="CGameConfig">
				<ConfigScriptResourceExpectedMaximums>
					<ExpectedMaximumsArray>
						<Item>
							<ResourceTypeName>PTFX</ResourceTypeName>
							<ExpectedMaximum value="122"/>
						</Item>
						<Item>
							<ResourceTypeName>PTFX_ASSET</ResourceTypeName>
							<ExpectedMaximum value="40"/>
						</Item>
						<Item>
							<ResourceTypeName>FIRE</ResourceTypeName>
							<ExpectedMaximum value="64"/>
						</Item>
						<Item>
							<ResourceTypeName>PEDGROUP</ResourceTypeName>
							<ExpectedMaximum value="16"/>
						</Item>
						<Item>
							<ResourceTypeName>SEQUENCE_TASK</ResourceTypeName>
							<ExpectedMaximum value="200"/>
						</Item>
						<Item>
							<ResourceTypeName>DECISION_MAKER</ResourceTypeName>
							<ExpectedMaximum value="20"/>
						</Item>
						<Item>
							<ResourceTypeName>CHECKPOINT</ResourceTypeName>
							<ExpectedMaximum value="61"/>
						</Item>
						<Item>
							<ResourceTypeName>TEXTURE_DICTIONARY</ResourceTypeName>
							<ExpectedMaximum value="100"/>
						</Item>
						<Item>
							<ResourceTypeName>DRAWABLE_DICTIONARY</ResourceTypeName>
							<ExpectedMaximum value="80"/>
						</Item>
						<Item>
							<ResourceTypeName>CLOTH_DICTIONARY</ResourceTypeName>
							<ExpectedMaximum value="2"/>
						</Item>
						<Item>
							<ResourceTypeName>FRAG_DICTIONARY</ResourceTypeName>
							<ExpectedMaximum value="44"/>
						</Item>
						<Item>
							<ResourceTypeName>DRAWABLE</ResourceTypeName>
							<ExpectedMaximum value="136"/>
						</Item>
						<Item>
							<ResourceTypeName>COVERPOINT</ResourceTypeName>
							<ExpectedMaximum value="51"/>
						</Item>
						<Item>
							<ResourceTypeName>ANIMATION</ResourceTypeName>
							<ExpectedMaximum value="57"/>
						</Item>
						<Item>
							<ResourceTypeName>MODEL</ResourceTypeName>
							<ExpectedMaximum value="700"/>
						</Item>
						<Item>
							<ResourceTypeName>RADAR_BLIP</ResourceTypeName>
							<ExpectedMaximum value="3600"/>
						</Item>
						<Item>
							<ResourceTypeName>ROPE</ResourceTypeName>
							<ExpectedMaximum value="36"/>
						</Item>
						<Item>
							<ResourceTypeName>CAMERA</ResourceTypeName>
							<ExpectedMaximum value="27"/>
						</Item>
						<Item>
							<ResourceTypeName>PATROL_ROUTE</ResourceTypeName>
							<ExpectedMaximum value="40"/>
						</Item>
						<Item>
							<ResourceTypeName>MLO</ResourceTypeName>
							<ExpectedMaximum value="35"/>
						</Item>
						<Item>
							<ResourceTypeName>RELATIONSHIP_GROUP</ResourceTypeName>
							<ExpectedMaximum value="502"/>
						</Item>
						<Item>
							<ResourceTypeName>SCALEFORM_MOVIE</ResourceTypeName>
							<ExpectedMaximum value="20"/>
						</Item>
						<Item>
							<ResourceTypeName>STREAMED_SCRIPT</ResourceTypeName>
							<ExpectedMaximum value="106"/>
						</Item>
						<Item>
							<ResourceTypeName>ITEM_SET</ResourceTypeName>
							<ExpectedMaximum value="6"/>
						</Item>
						<Item>
							<ResourceTypeName>VOLUME</ResourceTypeName>
							<ExpectedMaximum value="1"/>
						</Item>
						<Item>
							<ResourceTypeName>SPEED_ZONE</ResourceTypeName>
							<ExpectedMaximum value="220"/>
						</Item>
						<Item>
							<ResourceTypeName>WEAPON_ASSET</ResourceTypeName>
							<ExpectedMaximum value="124"/>
						</Item>
						<Item>
							<ResourceTypeName>VEHICLE_ASSET</ResourceTypeName>
							<ExpectedMaximum value="12"/>
						</Item>
						<Item>
							<ResourceTypeName>POPSCHEDULE_OVERRIDE</ResourceTypeName>
							<ExpectedMaximum value="1"/>
						</Item>
						<Item>
							<ResourceTypeName>POPSCHEDULE_OVERRIDE_VEHICLE_MODEL</ResourceTypeName>
							<ExpectedMaximum value="12"/>
						</Item>
						<Item>
							<ResourceTypeName>SCENARIO_BLOCKING_AREA</ResourceTypeName>
							<ExpectedMaximum value="36"/>
						</Item>
						<Item>
							<ResourceTypeName>BINK_MOVIE</ResourceTypeName>
							<ExpectedMaximum value="2"/>
						</Item>
						<Item>
							<ResourceTypeName>MOVIE_MESH_SET</ResourceTypeName>
							<ExpectedMaximum value="13"/>
						</Item>
						<Item>
							<ResourceTypeName>SET_REL_GROUP_DONT_AFFECT_WANTED_LEVEL</ResourceTypeName>
							<ExpectedMaximum value="6"/>
						</Item>
						<Item>
							<ResourceTypeName>VEHICLE_COMBAT_AVOIDANCE_AREA</ResourceTypeName>
							<ExpectedMaximum value="3"/>
						</Item>
						<Item>
							<ResourceTypeName>DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS</ResourceTypeName>
							<ExpectedMaximum value="3"/>
						</Item>
						<Item>
							<ResourceTypeName>DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS_MULTIPLIER</ResourceTypeName>
							<ExpectedMaximum value="3"/>
						</Item>
						<Item>
							<ResourceTypeName>SYNCED_SCENE</ResourceTypeName>
							<ExpectedMaximum value="51"/>
						</Item>
						<Item>
							<ResourceTypeName>CLIP_SET</ResourceTypeName>
							<ExpectedMaximum value="10"/>
						</Item>
						<Item>
							<ResourceTypeName>VEHICLE_RECORDING</ResourceTypeName>
							<ExpectedMaximum value="210"/>
						</Item>
						<Item>
							<ResourceTypeName>MOVEMENT_MODE_ASSET</ResourceTypeName>
							<ExpectedMaximum value="10"/>
						</Item>
						<Item>
							<ResourceTypeName>CUT_SCENE</ResourceTypeName>
							<ExpectedMaximum value="3"/>
						</Item>
						<Item>
							<ResourceTypeName>CUT_FILE</ResourceTypeName>
							<ExpectedMaximum value="3"/>
						</Item>
            <Item>
              <ResourceTypeName>GHOST_SETTINGS</ResourceTypeName>
              <ExpectedMaximum value="2"/>
            </Item>
            <Item>
              <ResourceTypeName>PICKUP_GENERATION_MULTIPLIER</ResourceTypeName>
              <ExpectedMaximum value="2"/>
            </Item>
          </ExpectedMaximumsArray>
				</ConfigScriptResourceExpectedMaximums>
			</Config>
		</Item>


	</ConfigArray>
</fwAllConfigs>

<!--
 Hash key, standard value, and structure reference guide below:
 
0x04FCE10C -          4 - caihandlinginfo
0x05293FA5 -          1 - audioheap
0x06EB2989 -          1 - ctaskusescenarioentityextension
0x07E95953 -          1 - attachmentextension
0x0995E411 -          1 - exprdictstore
0x0AA57FDE -          1 - networkdefstore
0x0C93E3D5 -         83 - camenvelope
0x0CF40089 -          1 - posematcherstore
0x0FD310BF -          1 - vehiclestruct
0x1116F36B -          1 - cgrabhelper
0x1182232C -         83 - cgamescripthandler
0x12C60340 -          1 - fwsimpletransform
0x13889110 -          1 - cscenariopointextradata
0x14984EE1 -          1 - scenariopoint
0x1996BA86 -        100 - cpatrollink
0x1A77B5AF -          1 - actiontable_interrelations
0x1B7BBEBE -          1 - cmoveanimatedbuilding
0x1BD2624F -          7 - ropedata
0x1BFCEF17 -          1 - fwmatrixtransform
0x1EB7AAE5 -          4 - camcollision
0x220EC274 -          1 - instancebuffer
0x22B81E14 -          1 - cprioritizedclipsetrequest
0x23B59B40 -          1 - actiontable_definitions
0x24852309 -          1 - interiorinst
0x24BEAD4E -          1 - cregenerationinfo
0x272E7F43 -          1 - portalinst
0x293949C9 -          1 - cclimbhandholddetected
0x2BD4DD73 -        215 - cscenarioinfo
0x2C1F0AC4 -          1 - ccombatinfo
0x2CDFE406 -          1 - staticbounds
0x2E968919 -          1 - animatedbuilding
0x2EB2EE6E -      10100 - navmeshes
0x2F040858 -        220 - cweaponcomponent
0x2FA3B9A2 -        111 - orders
0x2FEAD7A6 -        256 - fraginstnmgta
0x3066500C -          1 - fragmentstore
0x30A617DE -        900 - cscenariopoint
0x30DC3503 -          1 - fwquaterniontransform
0x32AA4601 -          1 - handlingdata
0x33818544 -          1 - ccombatsituation
0x348C3E40 -          1 - cscenarioclusterspawnedtrackingdata
0x39958261 -          1 - object
0x3A2BC128 -          1 - cweapon
0x3A2BC128 -       1024 - cweapon
0x3B8F741A -         64 - carmiksolver
0x3D211ECA -          4 - camspringmount
0x3EEA2DA9 -          1 - atdscriptobjectnode
0x3EF71716 -         33 - cplayerinfo
0x40CD8E90 -         10 - clegiksolver
0x411E7493 -         16 - cchathelper
0x4128232E -          1 - ccoverfinder
0x41663795 -       3000 - maxloadrequestedinfo
0x4380BD1E -         32 - crootslopefixupiksolver
0x43ED4D14 -          1 - tcbox
0x4821C9C1 -          1 - occlusionpathnode
0x489E6AC0 -          1 - actiontable_results
0x4C3A446E -          1 - ccargenforscenarios
0x4CF1D097 -          1 - framefilterstore
0x4D6735AE -          1 - ptfxsortedentity
0x4EC5AE40 -          1 - cambientlookat
0x4FE810E8 -         50 - cgamescripthandlernetwork
0x5047B2C4 -        256 - cmoveped
0x504FE2F5 -          2 - camcatchuphelper
0x528ACB56 -          1 - txdstore
0x529485A1 -          1 - interiorproxy
0x5411E15C -          1 - building
0x54753C86 -         60 - cvehiclestreamrequestgfx
0x5817CE07 -          1 - entitybatch
0x5A09F5F9 -          1 - cspclusterfsmwrapper
0x5E047C3E -        128 - vehicleglasscomponententity
0x652A20AF -        128 - targetting
0x670737C4 -          1 - cvehiclecombatavoidancearea
0x68065B7A -          1 - dwdstore
0x6851786C -       1600 - fraginstgta
0x69AAA6F7 -          1 - actiontable_homings
0x6E126610 -          1 - cprioritizedclipsetbucket
0x6E46CC34 -          2 - camthirdpersonframeinterpolator
0x6E63BFF3 -         50 - cpatrolnode
0x6F01D3C1 -          1 - vehiclescenarioattractors
0x72AAAC3F -          1 - cmoveobject
0x72FB71DA -          1 - compentity
0x737BAE9D -        512 - naenvironmentgroup
0x74AB6150 -          2 - camlookaheadhelper
0x74B31BE3 -          1 - vehicles
0x7567BA93 -          1 - animscenes
0x76BC4F20 -          1 - fwarchetypepooledmap
0x76F457EC -          1 - ctaskvehicleserialiserbase
0x7809CA42 -        256 - wptrec
0x7BA86481 -          1 - syncedscenes
0x7CB690F5 -          1 - actiontable_strikebones
0x7CBA2292 -         36 - caicurvepoint
0x7CD838AC -          1 - actiontable_impulses
0x7D347EE2 -          1 - actiontable_stealthkills
0x7E653152 -          1 - ccombatdirector
0x7FB0C46B -          1 - cambaseswitchhelper
0x80740EBE -          1 - mapdataloadednode
0x80CDD964 -          1 - scriptstore
0x80E83C46 -          1 - trafficlightinfos
0x8322BADD -          1 - maxnonregionscenariopointspatialobjects
0x86CA0EE2 -          1 - clothstore
0x8B11DC9F -       1250 - chandlingobject
0x8CAE847E -         32 - ctorsovehicleiksolverproxy
0x8CB13B20 -          1 - cgamescriptresource
0x8CC4F9DF -        150 - cpickupdata
0x8D748D4E -          1 - cscenariopointchainuseinfo
0x8DA12117 -          1 - peds
0x8DA12117 -        256 - peds
0x8DA54456 -          1 - cpropmanagementhelper
0x8DE0784B -        300 - crelationshipgroup
0x8E771F83 -          1 - cpathnoderoutesearchhelper
0x8F25956D -          1 - cgpsnumnodesstored
0x90D4BFF4 -          1 - vehiclestreamrequest
0x91323726 -          1 - actiontable_branches
0x938C2EA1 -          1 - animstore
0x940E3ABF -          1 - actiontable_damages
0x941F03C9 -          1 - drawablestore
0x94E57350 -        500 - fwdynamicentitycomponent
0x966BA3BC -          1 - scaleformmgrarray
0x975AC445 -       1500 - wheels
0x97930A24 -       1024 - clightextension
0x983A6EF3 -          1 - metadatastore
0x998F00AC -         34 - aircraftflames
0x999869F1 -          1 - ptfxassetstore
0x9AAD80FC -          1 - combatmountedmanager_attacks
0x9B36D076 -          1 - mapdatastore
0x9FE48203 -         13 - cdefaultcrimeinfo
0xA203EA4B -          1 - ctacticalanalysis
0xA53CA289 -          1 - cboatchasedirector
0xA7F63267 -         16 - ctorsoreactiksolver
0xA987CB1B -          1 - ccargen
0xAC9F5436 -        300 - cmovevehicle
0xAD2BCC1A -          1 - cpickup
0xB120A6BA -          1 - networkcrewdatamgr
0xB1786625 -          1 - cpickupplacementcustomscriptdata
0xB4419501 -          1 - maptypesstore
0xB442603D -          4 - camlookatdampinghelper
0xB4E04AA4 -         64 - cdoorextension
0xB758AEC3 -          1 - activeloadedinfo
0xB7D08969 -          1 - combatmeleemanager_groups
0xB7ED840D -          1 - cevent
0xB8EDE0CC -          1 - actiontable_vfx
0xB97089DE -          1 - objectintelligence
0xBAE33CCF -        410 - cweaponcomponentinfo
0xC2B5F089 -        100 - cvehiclestreamrendergfx
0xC3824168 -          1 - carrec
0xC50B0C6C -         16 - cbodylookiksolver
0xC5AACC92 -         64 - ctorsoiksolver
0xC732FB32 -          1 - activepersistentloadedinfo
0xC757E6CC -          1 - occlusionportalentity
0xCA211161 -          1 - lightentity
0xCC0AF84F -          1 - ctaskconversationhelper
0xCEBE5A3A -          2 - camhinthelper
0xD026E9A8 -         23 - camcontrolhelper
0xD21F4731 -          1 - occlusioninteriorinfo
0xD2F56334 -          1 - cvehiclechasedirector
0xD3312D41 -        500 - ceventnetwork
0xD64A10B7 -         40 - clegiksolverproxy
0xD6B42498 -         16 - ctorsovehicleiksolver
0xD7946DAB -         13 - cambaseframeshaker
0xD855984A -          1 - actiontable_facialanimsets
0xD866A500 -         40 - cbodylookiksolverproxy
0xD8D80132 -          1 - known refs
0xD9A77DFF -          1 - scaleformstore
0xDAA0A9E0 -          2 - caminconsistentbehaviourzoomhelper
0xDDBC66F5 -         51 - incidents
0xDFFC5283 -          1 - ctask
0xE010202B -       2600 - fwdynamicarchetypecomponent
0xE0A96C19 -          1 - decoratorextension
0xE0B50AA6 -          1 - grassbatch
0xE11D5267 -          1 - vehiclestreamrender
0xE3607A47 -         12 - camframeinterpolator
0xE4379A4C -         18 - explosiontype
0xE7509171 -        800 - quadtreenodes
0xEA0EC0E8 -          1 - occlusionportalinfo
0xEB9564E1 -       2234 - phinstgta
0xED9E8FD3 -         50 - cgamescripthandlernetcomponent
0xEE08D040 -          1 - cutscenestore
0xEF501806 -          1 - cpickupplacement
0xEF7129CB -          1 - cscriptentityextension
0xF17288D6 -          1 - dummy object
0xF2E37BE0 -          1 - maxloadedinfo
0xF66CA574 -          1 - navmeshroute
0xF72CC701 -          1 - croadblock
0xF8CCEE67 -         16 - cbodyrecoiliksolver
0xF9E1ECCC -          1 - actiontable_rumbles
0xFD0ABF92 -          1 - cstuntjump
0xFE12CE88 -         27 - cambasecamera
0xFE8E27D9 -         80 - camoscillator
0xFF74E9FD -          1 - cvehiclecliprequesthelper
0xFFD1343D -         40 - pointroute
0xE54EA79D -        600 - decorator
0xDF261E39 -       2000 - cinventoryitem
0xD7E71231 -          6 - patrolroute
0xD6F6816E -         64 - fwclothcollisionsextension
0xD29EB05B -        104 - fwcontainerlod
0xCFAEEE7A -       2389 - fwanimdirectorcomponentmotiontree
0xCA5ED810 -       1024 - fwanimdirector
0xC79C63D2 -       1024 - fwanimdirectorcomponentmove
0xBF69BB29 -        341 - fwanimdirectorcomponentragdoll
0xA38F3D93 -        255 - cspawnpointoverrideextension
0x9C085E2B -         32 - cnamedpatrolroute
0x857DA83E -          4 - ccollectioninfo
0x85FB462D -         50 - pedprop req data
0x74AB575B -          5 - atdtransactionnode
0x698208CF -       1200 - tasksequenceinfo
0x5F91F738 -          5 - netshoptransactions
0x5FA721B3 -          3 - ceventdecisionmakermodifiablecomponent
0x636873FE -        128 - cbullet::sbulletinstance
0x65087004 -         25 - ceventdecisionmaker
0x539C8EB8 -        120 - pedprop render data
0x490D814E -          4 - ceventdecisionmakerresponsedynamic
0x4A35D452 -        120 - shapetesttaskdata
0x4552434F -         60 - cbullet
0x40EAC531 -         31 - ctasksequencelist
0x3CC59946 -        682 - fwanimdirectorcomponentexpressions
0x36776CCA -       1024 - fwanimdirectorcomponentcreature
0x394AC584 -        256 - pedintelligence
0x30E4EADA -         15 - musicevent
0x302E7B2F -         10 - scriptshapetestresult
0x2D370C34 -        100 - streamped render data
0x210E10BE -        341 - fwanimdirectorcomponentfacialrig
0x16A315A2 -        341 - fwanimdirectorcomponentsyncedscene
0x0AB968F6 -         45 - streamped req data
0x3FA6EC68 -          1 - combatmeleemanager_groupsmp
0x4E2ADF9B -        128 - itemsetbuffer
0x7311A8D7 -        700 - fwscriptguid
0x45AAA13A -        480 - clandinggear_qkdfqq
0xB7750119 -        300 - cvehicleintelligence_8xo47n9 (appears to not use value here but instead from vehicle pool)
0xEB64ADF7 -          2 - collision_5plvhjd (doesn't appear to be actually used, needs more documentation)
0xFC5DD116 -          0 - MaxClothCollisionsExtensions (NOTE USED AS A POOL BUT A CONFIG2DEFFECTS ENTRY! doesn't appear to be actually used, needs more documentation)
 
 
 
0xC9F86984                  // rage__fwConfig
{
    0x351C1D6C  +0x08   Struct  (0) (PoolSizes)
}
 
0x279B988A                  // PoolSizes
{
    0xD566F590  +0x00   Array   (0) (Entries)
}
 
0x239608BB                  // PoolSizes Item
{
    0x46D34109  +0x00   String  (2) (PoolName)
    0xB2510AA8  +0x08   Int32   (0) (PoolSize)
}
 
0xFBC958E3  (CGameConfig)
{
    0xA796B8B4  +0x20   Struct  (0) (ConfigPopulation)
    0xF0345199  +0x2A4  Struct  (0) (Config2dEffects)
    0x09F9E8A1  +0x2F0  Struct  (0) (ConfigModelInfo)
    0x750FA764  +0x330  Struct  (0) (ConfigExtensions)
    0xA32B0E5D  +0x344  Struct  (0) (ConfigStreamingEngine)
    0x397F0EFD  +0x350  Struct  (0) (ConfigOnlineServices)
    0x316775A3  +0x380  Struct  (0) (ConfigUGCDescriptions)
    0x83DB96AD  +0x38C  Struct  (0) (ConfigNetScriptBroadcastData)
    0xFFBE95BF  +0x488  Struct  (0) (ConfigScriptStackSizes)
    0xA0261E4F  +0x498  Struct  (0) (ConfigScriptResourceExpectedMaximums)
    0xC4138B00  +0x4A8  Struct  (0) (ConfigScriptTextLines)
    0x012DA5E5  +0x4B8  Struct  (0) (ConfigMediaTranscoding)
    0xBEBA8D07  +0x4D8  Enum    (0) (UseVehicleBurnoutTexture)
    0x53F330C8  +0x4DC  Enum    (0) (AllowCrouchedMovement)
    0x04D0E9CD  +0x4E0  Enum    (0) (AllowParachuting)
    0x6AB03119  +0x4E4  Enum    (0) (AllowStealthMovement)
    0x7183A60B  +0x4E8  String  (2) (DebugScriptsPath)
    0x27A93DA5  +0x4C8  Map (0) (Threads)
}
 
0x3FC89C8A                  // ConfigPopulation
{
    0xD9CF0FFF  +0x00   Int32   (0) (ScenarioPedsMultiplier_Base)
    0xFEDDBB70  +0x04   Int32   (0) (ScenarioPedsMultiplier)
    0xF4E5DE24  +0x08   Int32   (0) (AmbientPedsMultiplier_Base)
    0x5B2AFB91  +0x0C   Int32   (0) (AmbientPedsMultiplier)
    0x9F950A3A  +0x10   Int32   (0) (MaxTotalPeds_Base)
    0xDF094B7B  +0x14   Int32   (0) (MaxTotalPeds)
    0xF5BD841B  +0x18   Int32   (0) (PedMemoryMultiplier)
    0x8720B5DE  +0x1C   Int32   (0) (PedsForVehicles_Base)
    0xFCE5F152  +0x20   Int32   (0) (PedsForVehicles)
    0x5D57B674  +0x24   Int32   (0) (VehicleTimesliceMaxUpdatesPerFrame_Base)
    0x18E03A5B  +0x28   Int32   (0) (VehicleTimesliceMaxUpdatesPerFrame)
    0xF10B4DCA  +0x2C   Int32   (0) (VehicleAmbientDensityMultiplier_Base)
    0x757865D5  +0x30   Int32   (0) (VehicleAmbientDensityMultiplier)
    0x6EBA2DD0  +0x34   Int32   (0) (VehicleMemoryMultiplier)
    0xDDBA1042  +0x38   Int32   (0) (VehicleParkedDensityMultiplier_Base)
    0x71642CA7  +0x3C   Int32   (0) (VehicleParkedDensityMultiplier)
    0x0C87399A  +0x40   Int32   (0) (VehicleLowPrioParkedDensityMultiplier_Base)
    0xFD2018DE  +0x44   Int32   (0) (VehicleLowPrioParkedDensityMultiplier)
    0x7B515286  +0x48   Int32   (0) (VehicleUpperLimit_Base)
    0x5AE21577  +0x4C   Int32   (0) (VehicleUpperLimit)
    0xA5B4C255  +0x50   Int32   (0) (VehicleUpperLimitMP)
    0x2B603009  +0x54   Int32   (0) (VehicleParkedUpperLimit_Base)
    0xC4501483  +0x58   Int32   (0) (VehicleParkedUpperLimit)
    0x9FE92A9E  +0x5C   Int32   (0) (VehicleKeyholeShapeInnerThickness_Base)
    0xB9461928  +0x60   Int32   (0) (VehicleKeyholeShapeInnerThickness)
    0x0663571F  +0x64   Int32   (0) (VehicleKeyholeShapeOuterThickness_Base)
    0x9A58C979  +0x68   Int32   (0) (VehicleKeyholeShapeOuterThickness)
    0x1BB85C3B  +0x6C   Int32   (0) (VehicleKeyholeShapeInnerRadius_Base)
    0xFFE11D0D  +0x70   Int32   (0) (VehicleKeyholeShapeInnerRadius)
    0x5A06121D  +0x74   Int32   (0) (VehicleKeyholeShapeOuterRadius_Base)
    0xAD7CA669  +0x78   Int32   (0) (VehicleKeyholeShapeOuterRadius)
    0x69DDB6A0  +0x7C   Int32   (0) (VehicleKeyholeSideWallThickness_Base)
    0xA279C15C  +0x80   Int32   (0) (VehicleKeyholeSideWallThickness)
    0x9821F579  +0x84   Int32   (0) (VehicleMaxCreationDistance_Base)
    0xD37DABC5  +0x88   Int32   (0) (VehicleMaxCreationDistance)
    0x788241DE  +0x8C   Int32   (0) (VehicleMaxCreationDistanceOffscreen_Base)
    0xD25FF31A  +0x90   Int32   (0) (VehicleMaxCreationDistanceOffscreen)
    0x07A29A3B  +0x94   Int32   (0) (VehicleCullRange_Base)
    0x9C46E576  +0x98   Int32   (0) (VehicleCullRange)
    0x9FCBE810  +0x9C   Int32   (0) (VehicleCullRangeOnScreenScale_Base)
    0xB05534B2  +0xA0   Int32   (0) (VehicleCullRangeOnScreenScale)
    0x3AABA635  +0xA4   Int32   (0) (VehicleCullRangeOffScreen_Base)
    0xF2B71420  +0xA8   Int32   (0) (VehicleCullRangeOffScreen)
    0xF704E670  +0xAC   Int32   (0) (DensityBasedRemovalRateScale_Base)
    0xFFDAE14A  +0xB0   Int32   (0) (DensityBasedRemovalRateScale)
    0x4FCEFAEB  +0xB4   Int32   (0) (DensityBasedRemovalTargetHeadroom_Base)
    0x3A947BF0  +0xB8   Int32   (0) (DensityBasedRemovalTargetHeadroom)
    0xD1A2DA92  +0xBC   Array   (4) (VehicleSpacing_Base)
    0x4264BA56  +0xFC   Array   (4) (VehicleSpacing)
    0xEED13578  +0x144  Array   (4) (PlayerRoadDensityInc_Base)
    0xA1334FAB  +0x184  Array   (4) (PlayerRoadDensityInc)
    0x43CCA0C3  +0x1C4  Array   (4) (NonPlayerRoadDensityDec_Base)
    0xF587F333  +0x204  Array   (4) (NonPlayerRoadDensityDec)
    0xBC717444  +0x13C  Int32   (0) (PlayersRoadScanDistance_Base)
    0x022FCD6B  +0x140  Int32   (0) (PlayersRoadScanDistance)
    0x469A83B4  +0x244  Int32   (0) (VehiclePopulationFrameRate_Base)
    0x869C4E41  +0x248  Int32   (0) (VehiclePopulationFrameRate)
    0xFB745AE7  +0x24C  Int32   (0) (VehiclePopulationCyclesPerFrame_Base)
    0xB32467EF  +0x250  Int32   (0) (VehiclePopulationCyclesPerFrame)
    0x4F5AD653  +0x254  Int32   (0) (VehiclePopulationFrameRateMP_Base)
    0x36FD709B  +0x258  Int32   (0) (VehiclePopulationFrameRateMP)
    0x8A9C4DE7  +0x25C  Int32   (0) (VehiclePopulationCyclesPerFrameMP_Base)
    0x5CF6A892  +0x260  Int32   (0) (VehiclePopulationCyclesPerFrameMP)
    0x338E1522  +0x264  Int32   (0) (PedPopulationFrameRate_Base)
    0x352031F9  +0x268  Int32   (0) (PedPopulationFrameRate)
    0x187FF165  +0x26C  Int32   (0) (PedPopulationCyclesPerFrame_Base)
    0xC0E77D97  +0x270  Int32   (0) (PedPopulationCyclesPerFrame)
    0x806FA648  +0x274  Int32   (0) (PedPopulationFrameRateMP_Base)
    0xD0DCB801  +0x278  Int32   (0) (PedPopulationFrameRateMP)
    0x3493303A  +0x27C  Int32   (0) (PedPopulationCyclesPerFrameMP_Base)
    0x7EB04E2E  +0x280  Int32   (0) (PedPopulationCyclesPerFrameMP)
}
 
0x1BC84E35                  // Config2dEffects
{
    0xBF216095  +0x00   Int32   (0) (MaxAttrsAudio)
    0x8AC7539E  +0x04   Int32   (0) (MaxAttrsBuoyancy)
    0x33DAC229  +0x08   Int32   (0) (MaxAttrsDecal)
    0xCB72E599  +0x0C   Int32   (0) (MaxAttrsExplosion)
    0xCEA093DA  +0x10   Int32   (0) (MaxAttrsLadder)
    0xF563FF57  +0x1C   Int32   (0) (MaxAttrsLightShaft)
    0xF178DB54  +0x20   Int32   (0) (MaxAttrsParticle)
    0xB3BE126D  +0x24   Int32   (0) (MaxAttrsProcObj)
    0x3BA272E0  +0x28   Int32   (0) (MaxAttrsScrollBar)
    0x57711DD0  +0x2C   Int32   (0) (MaxAttrsSpawnPoint)
    0xF0804147  +0x38   Int32   (0) (MaxAttrsWindDisturbance)
    0xCD6BB4FA  +0x3C   Int32   (0) (MaxAttrsWorldPoint)
    0xFC5DD116  +0x40   Int32   (0)
    0xF8C4FE9B  +0x44   Int32   (0) (MaxEffectsWorld2d)
}
 
0x7C6FF6B3                  // ConfigModelInfo
{
    0x9464955B  +0x00   String  (2) (defaultPlayerName)
    0x0CBBE225  +0x08   String  (2) (defaultProloguePlayerName)
    0xBF12376F  +0x10   Int32   (0) (MaxBaseModelInfos)
    0xCC94EA63  +0x14   Int32   (0) (MaxCompEntityModelInfos)
    0x7FE942AB  +0x18   Int32   (0) (MaxMloInstances)
    0x5CE32900  +0x1C   Int32   (0) (MaxMloModelInfos)
    0x93185D1E  +0x20   Int32   (0) (MaxPedModelInfos)
    0x7E5CBE81  +0x24   Int32   (0) (MaxTimeModelInfos)
    0xB2481040  +0x28   Int32   (0) (MaxVehicleModelInfos)
    0x39886DE3  +0x2C   Int32   (0) (MaxWeaponModelInfos)
    0x02482105  +0x30   Int32   (0) (MaxExtraPedModelInfos)
    0xA2D9B19A  +0x34   Int32   (0) (MaxExtraVehicleModelInfos)
    0x28D69F70  +0x38   Int32   (0) (MaxExtraWeaponModelInfos)
}
 
0x81ACA8F2                  // ConfigExtensions
{
    0xCC87ACEB  +0x00   Int32   (0) (MaxDoorExtensions)
    0x6DE85290  +0x04   Int32   (0) (MaxLightExtensions)
    0x1E9408A4  +0x08   Int32   (0) (MaxSpawnPointOverrideExtensions)
    0x664016AF  +0x0C   Int32   (0) (MaxExpressionExtensions)
    0xBDE77A4F  +0x10   Int32   (0)
}
 
0x777A46D6                  // ConfigStreamingEngine
{
    0x9E448195  +0x00   Int32   (0) (ArchiveCount)
    0x8B346D55  +0x04   Int32   (0) (PhysicalStreamingBuffer)
    0xAADCC446  +0x08   Int32   (0) (VirtualStreamingBuffer)
}
 
0x8EEB5461                  // ConfigOnlineServices
{
    0x88053E42  +0x00   String  (2) (RosTitleName)
    0xD5AA123A  +0x08   Int32   (0) (RosTitleVersion)
    0x74ED7C77  +0x0C   Int32   (0) (RosScVersion)
    0x5E713B76  +0x10   Int32   (0) (SteamAppId)
    0x3FE7E3A0  +0x18   String  (2) (TitleDirectoryName)
    0xFEF61BF6  +0x20   String  (2) (MultiplayerSessionTemplateName)
    0x2F257B8B  +0x28   String  (2) (ScAuthTitleId)
}
 
0x2B496E53                  // ConfigUGCDescriptions
{
    0x65C8E54A  +0x00   Int32   (0) (MaxDescriptionLength)
    0x8F3F4DD0  +0x04   Int32   (0) (MaxNumDescriptions)
    0xDAF5E2A7  +0x08   Int32   (0) (SizeOfDescriptionBuffer)
}
 
0x0BC2DDB5                  // ConfigNetScriptBroadcastData
{
    0x9FDE2BBE  +0x00   Array   (1) (HostBroadcastData)
    0xA8648A50  +0x7C   Array   (1) (PlayerBroadcastData)
}
 
0xE7C4CE05                  // BroadcastData Item
{
    0x73649489  +0x00   Int32   (0) (SizeOfData)
    0x3A369639  +0x04   Int32   (0) (MaxParticipants)
    0x173B6915  +0x08   Int32   (0) (NumInstances)
}
 
0xE1AEB06C                  // ConfigScriptStackSizes
{
    0x0F0F9C9A  +0x00   Array   (0) (StackSizeData)
}
 
0x3A9C1AD7                  // StackSizeData Item
{
    0x40758706  +0x00   String  (9) (StackName)
    0xC7D0C182  +0x04   Int32   (0) (SizeOfStack)
    0x8413ED1A  +0x08   Int32   (0) (NumberOfStacksOfThisSize)
}
 
0x9AC447B3                  // ConfigScriptResourceExpectedMaximums
{
    0x7E923F1C  +0x00   Array   (0) (ExpectedMaximumsArray)
}
 
0xA3358B19                  // ExpectedMaximumsArray Item
{
    0xE1A25872  +0x00   String  (9) (ResourceTypeName)
    0x17DCBF5A  +0x04   Int32   (0) (ExpectedMaximum)
}
 
0x3B34D3BB                  // ConfigScriptTextLines
{
    0xD8B0AFEF  +0x00   Array   (0) (ArrayOfMaximumTextLines)
}
 
0x2E9A2CFB                  // ArrayOfMaximumTextLines Item
{
    0x2DC2077E  +0x00   String  (9) (NameOfScriptTextLine)
    0x2D65178A  +0x04   Int32   (0) (MaximumNumber)
}
 
0x78970E5F                  // ConfigMediaTranscoding
{
    0x3373342A  +0x00   Int32   (0) (TranscodingSmallObjectBuffer)
    0xEF478EE3  +0x04   Int32   (0) (TranscodingSmallObjectMaxPointers)
    0x744A0C96  +0x08   Int32   (0) (TranscodingBuffer)
    0x3A600435  +0x0C   Int32   (0) (TranscodingMaxPointers)
}
 
0x53C3CC2E                  // Threads Item
{
    0x9F581BDD  +0x00   Enum    (0) (Priority)
    0x9347F4D6  +0x08   Array   (0) (CpuAffinity)
}
-->
'''

tf2config = '''
// Low preset
// Maximum performance without caring much about visibility or possible bugs
alias preset "exec presets/low"

lod=very_low
lighting=low
shadows=off
effects=very_low
water=low
particles=low
pyrovision=low
motion_blur=off
aa=off
post_processing=off
aa_msaa=off
texture_filter=bilinear
characters=very_low
decals=off
decals_models=off
decals_art=off
sprays=off
gibs=off
props=medium
ragdolls=off
3dsky=off
jigglebones=off
textures=very_low
texture_blending=off
bumpmap=off
specular=off
ropes=off
hud_player_model=off
xrays=off
sound=low

tf_quest_map_tuner_wobble_magnitude 0 // Disable the red tuner on the contracker
tf_item_inspect_model_auto_spin 0 // Do not auto spin items in the inspect view
tf_hud_target_id_show_avatars 0 // Never show avatars
tf_dashboard_slide_time 0 // Instant transitions
cl_crosshairalpha 255 // Disable transparency for lowend computers

echo "Low preset selected"'''

supportedGames = ["C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/GTA5.exe",
                  "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/hl2.exe"
                  ]

def Notify():
    root = Tk()
    root.geometry("500x200")
    root.title("ByrneOptimize")
    label1 = Label(root, text="Config Saved!")
    label1.config(font=("Times New Roman,", 32))
    label1.pack()

def Optimizer():
    if gui.filename == "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/GTA5.exe":
        cfg_file = open('C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/gta5.xml', 'w')
        cfg_file.write(gta5config)
        cfg_file.close()
        Notify()
    elif gui.filename == "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/hl2.exe":
        cfg_file = open('C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/cfg/low.cfg', 'w')
        cfg_file.write(tf2config)
        cfg_file.close()
        Notify()
