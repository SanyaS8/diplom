import { createStore } from "vuex";
import auth from "@/store/modules/auth.js";

export default createStore({
    modules: {
        auth
    }
})