<script>
  import { Router, Route } from "svelte-routing";

  import Index from "./routes/index.svelte";
  import Login from "./routes/login.svelte";
  import Message from "./routes/message.svelte"
</script>

<Router>
  <div>
    <Route path="/"><Index /></Route>
    <Route path="/login"><Login /></Route>
    <Route path="/message/:id" let:params><Message id="{params.id}"/></Route>
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