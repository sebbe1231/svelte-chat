<script>
    export let counter = 0;

    const plusOne = () => {
        counter++;
    }
</script>

<div style="text-align: center; display: flex; flex-direction: column; max-width: fit-content;">
    <b>Count is</b>
    <span>{counter}</span>
    <button on:click={plusOne}>+1</button>
</div>