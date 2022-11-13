<script>
  import { Router, Route, Link} from "svelte-routing";

  import Index from "./routes/index.svelte";
  import Login from "./routes/login.svelte";
</script>

<Router>
  <div>
    <Route path="/"><Index /></Route>
    <Route path="/login"><Login /></Route>
  </div>
</Router>

<!-- <script>
  import Counter from './lib/counter.svelte';

  let count;

  function updateCount() {
    count++;
  }
</script>

<h1>Velkommen til min sidea! {count}</h1>

<Counter bind:counter={count} /> -->