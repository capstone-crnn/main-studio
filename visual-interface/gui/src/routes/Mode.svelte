<script>
	// Imports
	import { link } from "svelte-spa-router";

</script>


<main class="container px-20 mx-auto">
	
	<div class="grid items-center grid-rows-3 gap-2">
		<h1 class="font-sans text-2xl font-bold text-center"> 
			Mode
		</h1>
		
		<div class="grid grid-cols-2 gap-2 place-items-center">
			<div class="pl-6">
				<h2 class="text-xl font-bold">
					Search & Rescue
				</h2>
				<p>Use this mode to detect nearby vital signs</p>
			</div>
			<a href="/search" use:link>
				<button class="p-4 rounded-md">
					<img src="graphics/human-resources-search-employees.svg" alt="Search" width="64px" />
				</button>
			</a>
		</div>
	
		<div class="grid grid-cols-2 gap-2 place-items-center">
			<div class="pl-6">
				<h2 class="text-xl font-bold">
					Monitor Vitals
				</h2>
				<p>Calibrate device to measure immediate vital signs</p>
			</div>
			<a href="/monitor" use:link>
				<button class="p-4 rounded-md">
					<img src="graphics/graph-stats-circle.svg" alt="Monitor" width="64px" />
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