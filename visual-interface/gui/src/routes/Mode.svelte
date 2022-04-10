<script>
	// Imports
	import { link } from "svelte-spa-router";

</script>


<main class="container px-40 mx-auto">
	
	<h1 class="pb-4 font-sans text-4xl font-normal text-center place-items-center"> 
		Mode
	</h1>

	<div class="grid items-center grid-rows-2 gap-2">
		
		<div class="grid grid-cols-3 gap-6 place-items-end">
			<div class="col-span-2 pb-4">
				<h2 class="text-3xl font-bold">
					Search & Rescue
				</h2>
				<p  class="pr-3 text-lg">Use this mode to detect nearby vital signs</p>
			</div>
			<a href="/search" use:link class="col-span-1">
				<button class="p-4 rounded-md">
					<img src="graphics/human-resources-search-employees.svg" alt="Search" width="96px" />
				</button>
			</a>
		</div>
	
		<div class="grid grid-cols-3 gap-6 place-items-end">
			<div class="col-span-2 pb-4">
				<h2 class="text-3xl font-bold">
					Monitor Vitals
				</h2>
				<p class="text-lg">Calibrate device to measure immediate vital signs</p>
			</div>
			<a href="/monitor" use:link class="col-span-1">
				<button class="p-4 rounded-md">
					<img src="graphics/graph-stats-circle.svg" alt="Monitor" width="96px" />
				</button>
			</a>
		</div>
	</div>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	
</style>