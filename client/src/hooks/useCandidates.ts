import { useState, useEffect } from "react";
import { fetchCandidates } from "../api";

const useCandidates = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [candidates, setCandidates] = useState<any[]>([]);

  const fetchCandidateData = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchCandidates();
      setCandidates(data.results);
    } catch (err) {
      setError("Failed to load Candidates.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCandidateData();
  }, []);

  return { candidates, loading, error };
};

export default useCandidates;
