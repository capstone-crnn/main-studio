<script>
	// Imports
	import { link } from "svelte-spa-router";

</script>

<main class="container h-full pt-10 mx-auto my-auto text-center">

	<div class="flex flex-row items-center justify-center">
		<img src="graphics/GroupS01_Logo-02-darker.svg" alt="Logo" class="inline w-64 pr-8 m-2 align-middle" />
		<div class="flex flex-col items-center justify-center">
			<h1 class="inline py-12 align-middle font-jetbrains text-7xl">
				finderFly
			</h1>
			<a href="/mode" use:link class="block rounded-3xl shadow-lg shadow-[#fcc100] font-sans tracking-wide font-light bg-[#fca232] text-white px-6 py-4 text-4xl w-full">
				START
			</a>
		</div>
	</div>
	<!-- <div class="pt-12">
		<img src="graphics/GroupS01_Logo-02-darker.svg" alt="Logo" class="inline m-2 align-middle w-36" />
		<h1 class="inline py-12 font-mono align-middle text-7xl">
			finderFly
		</h1>
	</div>
	<div class="items-center pt-6">
		<a href="/mode" use:link class="items-center block rounded-full mx-44 shadow-lg shadow-[#fcc100] font-sans tracking-wide font-light bg-[#fca232] text-white px-6 py-4 text-4xl">
				START
		</a>
	</div> -->
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

	h1 { 
		color: #fca232;
	}

	@font-face {
		font-family: 'JetBrains Mono', monospace;
		src: url("fonts/JetBrainsMonoNL-Regular.ttf");
	}
</style>