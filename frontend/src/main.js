import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "bootstrap/dist/css/bootstrap.min.css";
import router from "./routers.js";

const app = createApp(App);

app.use(router);

createApp(App).mount("#app");
