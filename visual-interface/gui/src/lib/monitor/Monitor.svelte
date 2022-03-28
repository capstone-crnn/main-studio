<script>
	// Imports
	import { bpmData } from './../../stores/stores.js';
	import ActionBar from "../../common/ActionBar.svelte";
	import StatusBar from "../../common/StatusBar.svelte";
	import MonitorGraph from "./MonitorGraph.svelte";
	import MonitorMetrics from "./MonitorMetrics.svelte";


	let bpmLungs = 12;
	let bpmHeart = 92;

	let distance = 0.7;		// meters
	let timeElapsed = 4;	// hours
	
	let isReady = false;
	let isCalibrating = false;
	let displayHeart = false;
	let displayLungs = false;
	let statusText = "Ready for calibration";
	let statusIcon = "ready.svg";
	
	// States
	$: hideGraph = true;
	$: actionBarConfig = [
		{
			text: "Calibrate",
			image: "rec.svg",
			disabled: false,
			action: () => { 
				isCalibrating = true;
				isReady = false; 
				hideGraph = true;
				statusText = "Connecting...";
				statusIcon = "loading.svg";
				bpmData.set([]);
			}
		},
		{
			text: "Heart",
			image: "heart-attack.svg",
			disabled: !isReady || displayHeart,
			action: () => { 
				displayHeart = true;
				displayLungs = false;
			}
		},
		{
			text: "Lungs",
			image: "human-lungs.svg",
			disabled: !isReady || displayLungs,
			action: () => { 
				displayHeart = false;
				displayLungs = true;
			}
		}
	]

	// Processing and storing data
	api.Stream((evt, data) => {
		// console.log("Data: ", data);
		// if (data && data[0] && data[0] !== 0) {
		if (data) {
			bpmLungs = data;
			let now = new Date().toLocaleTimeString('en-US', { 
					hour12: false, 
					hour: "numeric", 
					minute: "numeric",
					second: "numeric"
			});
			
			console.log($bpmData.length);
			if ($bpmData.length >= 100){
				$bpmData = [...$bpmData.slice(1), {
				value: data,
				time: now
				}];
			} else {
				$bpmData = [...$bpmData, {
					value: data,
					time: now
				}];
			}
		}
	});

</script>


<main>
	<ActionBar config={actionBarConfig} dir="left" class="self-stretch"/>
	
	<div class="container grid grid-cols-3 gap-1 pl-20">
		
		
		{#if !isReady && !isCalibrating}
			<div id="calibration" class="pt-8">
				<h2>Touch to calibrate</h2>	
			</div>
		{:else if !isReady && isCalibrating}
			<div id="calibration" class="pt-8">
				<div class="h-full text-center align-middle border-2 rounded-full">
					<h2> Calibrating... </h2>
					<button on:click={() => {
						isReady = true;
						statusText = "Connected";
						statusIcon = "check-mark.svg";
						displayHeart = true;
						hideGraph = false;
					}}>
						Ready
					</button>
				</div>	
			</div>
		{:else if (isReady && displayHeart)}
			<MonitorMetrics type="heart" metrics={{
				bpm: bpmHeart,
				distance,
				timeElapsed
			}} />
		{:else if (isReady && displayLungs)}
			<MonitorMetrics type="lungs" metrics={{
				bpm: bpmLungs,
				distance,
				timeElapsed
			}} />
		{/if}
		
		<div class="col-span-2 overflow-hidden">
			<MonitorGraph {hideGraph} />
		</div>

	</div>

	<StatusBar {statusText} {statusIcon} />

	
	
</main>


<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>