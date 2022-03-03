<script>
	// Imports
	import { afterUpdate } from "svelte";
	import Chart from "chart.js/auto";
	
	import * as subjectData from "../../data/subject4.js";	// TODO: temp data, remove later
	
	// Props
	export let hideGraph;
	
	const data = subjectData.default;
	const xValues = data.map((d) => d["X_Value"]);	
	const yValues = data.map((d) => d["radar24-I"]);

	let ctx;
	let chartCanvas;
	let chartTarget;

	// States
	$: config = {
			type: 'line',
			data: {
				// showLine: false,
				labels: xValues,
				datasets: [{
					label: "BPM",
					hidden: hideGraph,
					backgroundColor: 'rgb(255, 99, 40)',
					borderColor: 'rgb(255, 99, 40)',
					data: yValues
				}]
			},
			options: {
				animation: {
					duration: 0
				}
			}
		};

	afterUpdate(async (promise) => {
		if (chartTarget) {
			chartTarget.destroy();
		}
	
		ctx = chartCanvas.getContext('2d');
		chartTarget = new Chart(ctx, config);
	});
	
</script>

<canvas bind:this={chartCanvas} id="myChart"></canvas>


<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

	
</style>