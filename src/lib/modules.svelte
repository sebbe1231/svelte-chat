<script>
    import { onMount } from "svelte";

    let modules = null;

    onMount(async () => {
        const data = await fetch("/api/getModules").then(resp => resp.json())

        modules = data.modules;
    })
</script>

{#if modules === null}
    Loading...
{:else if modules.length === 0}
    Ingen moduler...
{:else}
    {#each modules as module}
        <div>
            <h1>{module.title}</h1>
            <p>{modules.description}</p>
        </div>
    {/each}
{/if}