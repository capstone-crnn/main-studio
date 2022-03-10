<script>
	// Imports
	import ActionBar from "../../common/ActionBar.svelte";


	
	// States
	$: logs = [];	
	$: actionBarConfig = [
		{
			text: "Play",
			image: "play-button-arrowhead.svg",
			disabled: false,
			action: () => {}
		},
		{
			text: "Stop",
			image: "stop.svg",
			disabled: false,
			action: () => {}
		},
		{
			text: "Capture",
			image: "photo-capture.svg",
			disabled: false,
			action: () => {
				const now = new Date().toLocaleTimeString('en-US', { 
					hour12: false, 
					hour: "numeric", 
					minute: "numeric",
					second: "numeric"
				});
				logs = [ { time: now, distance: Math.random().toFixed(2) }, ...logs];
			}
		},
		{
			text: "Delete",
			image: "delete.svg",
			disabled: false,
			action: () => {
				logs = [];
			}
		}
	]
</script>

<main>

	<div class="grid max-h-full grid-cols-7 gap-1">
		<!-- <h1>Search</h1> -->
		<div class="col-span-2 ml-2">
			<h3 class="text-xl italic font-bold">
				Last spotted:
			</h3>
			{#each logs as log }
				<p> {log.time} | <span class="font-bold">{log.distance}m</span></p>
			{:else}
				<p>—</p>
			{/each}
		</div>
	
		<div class="col-span-4 place-items-center">
			<h2>Initiate search</h2>
			<p>Touch the play icon</p>
		</div>
	

		<ActionBar config={actionBarConfig} dir="right" />
	</div>


</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	

	h1 {
		/* color: #ff3e00; */
		color: #F28E44;
		/* text-transform: uppercase; */
		font-size: 4em;
		font-weight: 100;
	}
</style>