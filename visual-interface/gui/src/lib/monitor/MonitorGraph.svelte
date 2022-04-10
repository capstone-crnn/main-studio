<script>
	// Imports
	import { afterUpdate } from "svelte";
	import Chart from "chart.js/auto";
	import { bpmData } from './../../stores/stores.js';

	// Props
	export let hideGraph;

	let ctx;
	let chartCanvas;
	let chartTarget;


	$: data = $bpmData;
	$: xValues = data.map((d) => d["time"]);	
	$: yValues = data.map((d) => d["value"]);

	// States
	$: config = {
			type: 'line',
			data: {
				// showLine: false,
				labels: hideGraph? [] : xValues,
				datasets: [{
					label: "BPM",
					hidden: hideGraph,
					backgroundColor: 'rgb(255, 99, 40)',
					borderColor: 'rgb(255, 99, 40)',
					data: yValues,
					fill: {
						target: 'start',
						above: 'rgb(255, 99, 40,0.2)'
					},
					pointRadius: 0,
					lineTension: 0.4
				}]
			},
			options: {
				interaction: {
      				intersect: false,
    			},
				animation: {
					duration: 0
				},
				scales: {
					y: {
						suggestedMin: 10,    // minimum unless there is a lower value.
						suggestedMax: 20,    // maximum unless there is a higher value.
					}
				},
				plugins: {
					legend: {
						display: false
					}
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