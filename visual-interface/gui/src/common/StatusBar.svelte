<script>
	export let statusText, statusIcon;
</script>

<div>
	<aside class="fixed bottom-0 flex items-center w-full">
		<div class="flex flex-row justify-between w-full h-16 ml-20 border-t-2 border-l-2 rounded-tl-3xl">
			<div class="self-center inline">
				<h3 class="px-6 font-sans text-3xl italic font-light">
					{statusText}
				</h3>
			</div>
			<div class="mt-4 mb-2 mr-4">
				<img src="graphics/{statusIcon}" alt="{statusText}" class="w-8"/>
			</div>
		</div>
	</aside>
</div>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	
</style>