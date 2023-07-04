// store.js
import { createStore } from "vuex";

const store = createStore({
  state() {
    return {
      admin: false
    };
  },
  mutations: {
    setAdmin(state, value) {
      state.admin = value;
    }
  },
  actions: {
    setAdmin(context, value) {
      context.commit("setAdmin", value);
    }
  },
  getters: {}
});

export default store;