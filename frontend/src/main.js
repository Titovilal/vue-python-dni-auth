import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "bootstrap/dist/css/bootstrap.min.css";
import router from "./routers";
import store from "./store";

const app = createApp(App);
app.use(router);
app.use(store);
app.mount("#app");


