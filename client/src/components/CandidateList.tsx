import CandidateCard from "./CandidateCard";
import useCanditates from "../hooks/useCandidates";

const CandidateList = () => {
  const { candidates, loading } = useCanditates();

  return (
    <div>
      {loading ? (
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            marginTop: "20px",
          }}
        >
          "Loading"
        </div>
      ) : candidates?.length > 0 ? (
        candidates.map((candidate: any) => (
          <span key={candidate.name}>
            <CandidateCard candidate={candidate} />
          </span>
        ))
      ) : (
        "No Candidates found..."
      )}
    </div>
  );
};

export default CandidateList;
