<script>
	// Imports
	import ActionBar from "../../common/ActionBar.svelte";


	let isSearching = false;
	let isInitiated = false;
	let isDetected;
	
	// States
	$: logs = [];	
	// $: isDetected = 0;
	$: actionBarConfig = [
		{
			text: "Play",
			image: "play-button-arrowhead.svg",
			disabled: false,
			action: () => {
				isSearching = true;
				isInitiated = true;
			}
		},
		{
			text: "Stop",
			image: "stop.svg",
			disabled: false,
			action: () => {
				isInitiated = false;
				isSearching = false;
			}
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
				logs = [ { time: now, detection: (isDetected && isDetected === 1) ? "detected" : "-"  }, ...logs];
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


	// Processing and storing data
	api.Stream((evt, data) => {
		if (data && data[2]) { 
			isDetected = data[2];
			if (isDetected && isDetected === 1) {
				const now = new Date().toLocaleTimeString('en-US', { 
						hour12: false, 
						hour: "numeric", 
						minute: "numeric",
						second: "numeric"
					});
				logs = [ { time: now, detection: isDetected === 1 ? "detected" : "none" }, ...logs];
			}
		}
	});
</script>

<main>
	<h1 class="fixed text-4xl font-extralight top-2 left-20">
		<span class="font-bold">Mode</span> — Search
	</h1>
	<div class="grid max-h-full grid-cols-7 gap-1 pl-4 truncate">
		<div class="col-span-2 ml-2 h-80">
			<h3 class="pt-6 text-2xl italic font-bold">
				Last spotted:
			</h3>
			{#each logs as log }
				<p class="pb-1 text-lg">
					{log.time} | <span class="font-bold">{log.detection}</span>
				</p>
			{:else}
				<p class="text-lg">—</p>
			{/each}
		</div>
	
		<div class="w-full h-full col-span-4 rounded-full shadow-inner border-dotted  border-4 {isDetected ? "border-yellow-500 bg-orange-50" : ""}">
			{#if !isInitiated}
				<div class="flex flex-col items-center justify-center h-full">
					<h2 class="text-4xl font-light">
						Initiate search
					</h2>
					<p class="text-lg italic">
						Touch the play icon
					</p>
				</div>
			{:else if isInitiated && isSearching}
				<div class="flex flex-col items-center justify-center h-full">
					{#if (isDetected && isDetected === 1)}
						<h2 class="text-4xl font-semibold">
							<p>Detected</p>
							<p>human ahead!</p>
						</h2>
					{:else}
						<h2 class="text-4xl italic font-light">
							Searching...
						</h2>
					{/if}
				</div>
			{/if}
		</div>
	

		<ActionBar config={actionBarConfig} dir="right" />
	</div>


</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	

	h1 {
		color: #fca232;
		font-size: 4em;
		font-weight: 100;
	}	
	
</style>