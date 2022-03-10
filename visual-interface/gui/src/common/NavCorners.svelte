<script>
	// Imports
	import { afterUpdate } from "svelte";
	import { link, location } from "svelte-spa-router";

	let currentPath;
	afterUpdate(() => {
		currentPath = $location;
	})

</script>


<div class="flex items-center w-full">
	<div class="flex flex-row justify-end w-full">
		<div class="inline rotate-90 border-b-2 border-r-2 rounded-br-3xl">
			<img src="graphics/battery-status-full.svg" alt="Battery Status" class="w-12 m-2" /> 
		</div> <!--TODO: add dynamic battery status -->
	</div>
</div>


<!-- TODO: clean up -->
<div class="fixed flex flex-wrap justify-between h-full bottom-1">
	<div class="flex flex-col justify-between">
		{#if currentPath === "/"}
			<a href="/" class="inline border-b-2 border-r-2 rounded-br-3xl" use:link on:click={() => window.api.PowerOff()}>
				<img src="graphics/power-button.svg" alt="Power Off" class="w-12 m-2" />
			</a>
			
		{:else}
			{#if currentPath === "/mode"}
				<a href="/" class="inline border-b-2 border-r-2 rounded-br-3xl" use:link>
					<img src="graphics/back.svg" alt="Back" class="w-12 m-2" />
				</a>
				<a href="/" class="inline border-t-2 border-r-2 rounded-tr-3xl" use:link>
					<img src="graphics/homepage.svg" alt="Home" class="w-12 m-2" />
				</a>
			{:else}
				<a href="/mode" class="inline border-b-2 border-r-2 rounded-br-3xl" use:link>
					<img src="graphics/back.svg" alt="Back" class="w-12 m-2" />
				</a>
				<a href="/" class="inline border-t-2 border-r-2 rounded-tr-3xl" use:link>
					<img src="graphics/homepage.svg" alt="Home" class="w-12 m-2" />
				</a>
			{/if}
		{/if}
	</div>
</div>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>