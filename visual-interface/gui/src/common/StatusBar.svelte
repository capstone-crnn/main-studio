<script>
	export let statusText;
</script>

<aside>
	<h3>{statusText}</h3>
	<!--TODO: add icon -->
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