import axios from "axios";

const API_URL = "http://localhost:8080/api/all";

export const fetchCandidates = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error("Error fetching candidates:", error);
    throw error;
  }
};
