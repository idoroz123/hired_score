// Candidate Props
type CandidateExperience = {
  title: string;
  start_date: string;
  end_date: string;
  gap?: string;
};

type CandidateProps = {
  name: string;
  experience: CandidateExperience[];
};

type CandidateCardProps = {
  candidate?: CandidateProps;
};

const CandidateCard = ({ candidate }: CandidateCardProps) => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        textAlign: "left",
        border: "2px solid white",
      }}
    >
      <p>Name: {candidate?.name}</p>
      {candidate?.experience && candidate.experience.length > 0 ? (
        candidate.experience.map((exp, index) => (
          <div key={index} style={{ marginBottom: "10px" }}>
            <p>
              Worked as: {exp.title}, From: {exp.start_date}, To: {exp.end_date}
            </p>
            {exp.gap && <p>Gap: {exp.gap}</p>}
          </div>
        ))
      ) : (
        <p>No experience available</p>
      )}
    </div>
  );
};

export default CandidateCard;
