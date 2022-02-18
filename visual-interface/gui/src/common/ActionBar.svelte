<script>
	// Props
	// export let direction;
	export let config;
</script>

<aside>
	{#each config as btn }
		<button alt={btn.text} on:click={btn.action} disabled={btn.disabled}>
			<!-- TODO: add icons -->
			{btn.text}
		</button>
	{/each}
</aside>

<style global lang="postcss">
	@tailwind base;
  	@tailwind components;
  	@tailwind utilities;

	aside { 
		border-style: solid;
		border-width: 0.05rem;
		border-radius: 0.50rem;
	}
</style>