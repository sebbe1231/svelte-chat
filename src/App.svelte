<script>
  import Counter from './lib/counter.svelte';

  let count;

  function updateCount() {
    count++;
  }
</script>

<h1>Velkommen til min sidea! {count}</h1>

<Counter bind:counter={count} />