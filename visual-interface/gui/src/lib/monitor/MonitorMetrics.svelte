<script>
    // Props
    export let type;
    export let metrics;
</script>


<div id="metrics-{type}" class="pt-8 pl-8">
    <h2 class="text-3xl font-extrabold">
        {metrics.bpm} <span class="font-normal">bpm</span>
    </h2>
    <h3 class="text-2xl italic font-light">
        {#if type === "heart"}
            Heart rate
        {:else if type === "lungs"}
            Respiratory rate
        {/if}
    </h3>
    
    <h2 class="pt-8 text-3xl font-extrabold">
        {metrics.distance} <span class="font-normal">m</span>
    </h2>
    <h3 class="text-2xl italic font-light">
        Distance
    </h3>	
    
    <h2 class="pt-8 text-3xl font-extrabold">
        {metrics.timeElapsed}
    </h2>
    <h3 class="text-2xl italic font-light">
        Time elapsed
    </h3>	
</div>


<style global lang="postcss">
    @tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>