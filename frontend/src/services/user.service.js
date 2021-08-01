import axios from "axios";
import authHeader from "./auth-header";

const API_URL = "/v1/";

const getAllLents = () => {
  return axios.get(API_URL + "lent", { headers: authHeader() });
};

const addLent = (to, description, amount, currency, due_date) => {
  return axios.post(API_URL + "lent", {
    to,
    description,
    amount,
    currency,
    due_date,
  }, { headers: authHeader() });
};

export default {
    getAllLents,
    addLent,
};