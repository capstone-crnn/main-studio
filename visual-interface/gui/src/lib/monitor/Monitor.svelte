<script>
	// Imports
	import ActionBar from "../../common/ActionBar.svelte";
	import StatusBar from "../../common/StatusBar.svelte";
	import MonitorGraph from "../monitor/MonitorGraph.svelte";


	let bpmLungs = 12;
	let bpmHeart = 92;

	let distance = 0.7;		// meters
	let timeElapsed = 4;	// hours
	
	// States
	$: isReady = false;
	$: isCalibrating = false;
	$: displayHeart = false;
	$: displayLungs = false;
	$: statusText = "Ready for calibration";

	$: actionBarConfig = [
		{
			text: "Calibrate",
			disabled: false,
			action: () => { 
				isCalibrating = true;
				isReady = false; 
				statusText = "Connecting...";
			}
		},
		{
			text: "Heart",
			disabled: !isReady || displayHeart,
			action: () => { 
				displayHeart = true;
				displayLungs = false;
			}
		},
		{
			text: "Lungs",
			disabled: !isReady || displayLungs,
			action: () => { 
				displayHeart = false;
				displayLungs = true;
			}
		}
	]

</script>

<main>
	<h1>Monitor</h1>

	{#if !isReady && !isCalibrating}
		<div id="calibration">
			<h2>Touch to calibrate</h2>	
		</div>
	{:else if !isReady && isCalibrating}
		<div id="calibration">
			<h2>Calibrating...</h2>	
			<button on:click={() => {
				isReady = true;
				statusText = "Connected";
				displayHeart = true;
			}}>
				Ready
			</button>
		</div>
	{:else if (isReady && displayHeart)}
		<div id="metrics-heart">
			<h2>{bpmHeart}bpm</h2>
			<h3>Heart rate</h3>
			
			<h2>{distance}m</h2>
			<h3>Distance</h3>	
			
			<h2>{timeElapsed}hrs</h2>
			<h3>Time elapsed</h3>	
		</div>
	{:else if (isReady && displayLungs)}
		<div id="metrics-lungs">
			<h2>{bpmLungs}bpm</h2>
			<h3>Respiratory rate</h3>
			
			<h2>{distance}m</h2>
			<h3>Distance</h3>	
			
			<h2>{timeElapsed}hrs</h2>
			<h3>Time elapsed</h3>	
		</div>
	{/if}

	<!-- <MonitorGraph /> -->

	<ActionBar config={actionBarConfig} />
	<StatusBar {statusText} />
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
</style>