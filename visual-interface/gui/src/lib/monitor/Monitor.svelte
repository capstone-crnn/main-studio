<script>
	// Imports
	import { onDestroy } from "svelte";
	import { bpmData } from './../../stores/stores.js';
	import ActionBar from "../../common/ActionBar.svelte";
	import StatusBar from "../../common/StatusBar.svelte";
	import MonitorGraph from "./MonitorGraph.svelte";
	import MonitorMetrics from "./MonitorMetrics.svelte";


	let bpmLungs = "—";
	let bpmHeart = "—";

	let distance = "—";
	let startTime;

	let isReady = false;
	let isCalibrating = false;
	
	let displayHeart = false;
	let displayLungs = false;
	
	let statusText = "Ready for calibration";
	let statusIcon = "ready.svg";
	let statusAnimated = false;
	
	// States
	$: isDetected = false;
	$: timeElapsed = "00:00:00";
	$: hideGraph = true;
	$: actionBarConfig = [
			{
					text: "Calibrate",
					image: "rec.svg",
					disabled: false,
					animated: !isCalibrating && !isReady,
					action: () => {
							isCalibrating = true;
							isReady = false;
							hideGraph = true;
							statusText = "Connecting...";
							statusIcon = "loading.svg";
							statusAnimated = true;
							bpmData.set([]);
							window.api.Calibrate();

							setTimeout(() => {
									isReady = true;
									statusText = "Connected";
									statusIcon = "check-mark.svg";
									// displayHeart = true;
									displayLungs = true;
									hideGraph = false;
									statusAnimated = false;

									startTime = new Date();
							}, 5000);
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
			if (data && data[2] == 0) {
				isDetected = false;
				bpmLungs = "—";
				bpmHeart = "—";

				let now = new Date().toLocaleTimeString('en-US', {
					hour12: false,
					hour: "numeric",
					minute: "numeric",
					second: "numeric"
				});

				if ($bpmData.length >= 100){
						$bpmData = [...$bpmData.slice(1), {
						value: 0,
						time: now
						}];
				} else {
						$bpmData = [...$bpmData, {
								value: 0,
								time: now
						}];
				}
			} else {
				isDetected = true;
				if (data && data[0]) {
						bpmLungs = data[0].toFixed(2);
						let now = new Date().toLocaleTimeString('en-US', {
							hour12: false,
							hour: "numeric",
							minute: "numeric",
							second: "numeric"
						});
						if ($bpmData.length >= 100){
								$bpmData = [...$bpmData.slice(1), {
								value: data[0],
								time: now
								}];
						} else {
								$bpmData = [...$bpmData, {
										value: data[0],
										time: now
								}];
						}
				}
			}
	});

	const interval = setInterval(() => {
			if (startTime) {
					let now = new Date();
					let seconds, minutes, hours;

					timeElapsed = now - startTime;
					timeElapsed /= 1000;
					seconds = Math.floor(timeElapsed % 60);
					timeElapsed = Math.floor(timeElapsed / 60);
					minutes = Math.floor(timeElapsed % 60);
					timeElapsed = Math.floor(timeElapsed / 60);
					hours = Math.floor(timeElapsed % 24);

					timeElapsed = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
			}

	}, 1000);

	onDestroy(() => {
			clearInterval(interval);
	});


</script>


<main>
	<ActionBar config={actionBarConfig} dir="left" class="self-stretch"/>
	<h1 class="fixed text-4xl font-extralight top-2 left-20">
			<span class="font-bold">Mode</span> — Monitor
	</h1>
	<div class="container grid grid-cols-3 gap-1 pl-20">


			{#if !isReady && !isCalibrating}
					<div id="calibration" class="pt-10 text-xl font-normal text-gray-400">
							<h2 class="italic animate-pulse"> Touch to</h2>
							<h2 class="italic animate-pulse"> calibrate</h2>
					</div>
			{:else if !isReady && isCalibrating}
					<div id="calibration" class="rounded-full shadow-inner">
							<!-- <div class="h-full text-center align-middle border-2 rounded-full">
									<h2> Calibrating... </h2>
							</div> -->
							<div class="flex flex-col items-center justify-center h-full">
								<h2 class="text-2xl font-light">
									Calibrating...
								</h2>
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
					{#if !isDetected & isReady}
						<div class="px-4 py-3 mt-6 text-2xl text-red-700 bg-red-100 border border-red-400 rounded-md">
							<p>No vital signs detected!</p>
						</div>
					{/if}
			</div>

	</div>

	<StatusBar {statusText} {statusIcon} {statusAnimated} />



</main>


<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>