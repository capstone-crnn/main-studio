<script>
	// Props
	export let config;
	export let dir;
</script>


{#if dir === "left" }
	<aside class="fixed flex h-2/3 left-0 border-2 rounded-r-3xl z-[999] justify-evenly mt-2">
		<div class="flex flex-col w-full justify-evenly">
			{#each config as btn (btn.text) }
				<button 
					alt={btn.text} 
					on:click={btn.action} 
					disabled={btn.disabled}
					class="border-none"
				>
					<img src="graphics/{btn.image}" alt="{btn.text}" class="w-12 max-w-5xl m-2 {btn.disabled ? "opacity-25" : ""}"/>
				</button>
			{/each}
		</div>
	</aside>
{:else if dir === "right"}
	<aside class="fixed flex h-2/3 right-0 border-2 rounded-l-3xl z-[999] justify-evenly mt-2">
		<div class="flex flex-col w-full justify-evenly">
			{#each config as btn (btn.text) }
				<button 
					alt={btn.text} 
					on:click={btn.action} 
					disabled={btn.disabled}
					class="border-none"
				>
					<img src="graphics/{btn.image}" alt="{btn.text}" class="w-12 max-w-5xl m-2 {btn.disabled ? "opacity-25" : ""}"/>
				</button>
			{/each}
		</div>
	</aside>
{/if}


<style global lang="postcss">
	@tailwind base;
  	@tailwind components;
  	@tailwind utilities;

</style>