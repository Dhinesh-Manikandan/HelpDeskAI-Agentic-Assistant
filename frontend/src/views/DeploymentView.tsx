export default function DeploymentView() {
    return (
        <div className="p-8 max-w-4xl">
            <h2 className="text-3xl font-bold mb-6">Deployment Strategy</h2>
            <div className="bg-surface p-8 rounded-xl border border-slate-700 prose prose-invert max-w-none">
                <h3>Current Demo Implementation</h3>
                <p>React + Vite frontend served via Node. Spring Boot backend running on local Tomcat. SQLite database.</p>
                <h3>Proposed Enterprise Deployment</h3>
                <ul>
                    <li><strong>Frontend:</strong> React built as static assets, served via CDN or Nginx container.</li>
                    <li><strong>Backend:</strong> Spring Boot application containerized via Docker.</li>
                    <li><strong>Database:</strong> PostgreSQL cluster with read replicas for high availability.</li>
                    <li><strong>Orchestration:</strong> Kubernetes cluster for autoscaling and self-healing.</li>
                </ul>
            </div>
        </div>
    );
}
