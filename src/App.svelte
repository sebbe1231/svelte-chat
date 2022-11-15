<script>
  import { Router, Route, Link} from "svelte-routing";
  import { user } from "./lib/stores"

  import Index from "./routes/index.svelte";
  import Login from "./routes/login.svelte";

  fetch("/getuser", {
    method: "GET"
  }).then(resp => resp.json()).then(data => {
    if(data["status"] === true){
      user.set(data["data"])
    }
  })
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