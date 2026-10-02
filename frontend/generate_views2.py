import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/frontend/src/views"

views = {
    "HistoryView.tsx": """import { useState, useEffect } from 'react';
import axios from 'axios';

export default function HistoryView() {
    const [tasks, setTasks] = useState<any[]>([]);
    
    useEffect(() => {
        axios.get('http://localhost:8080/api/agent/tasks').then(res => setTasks(res.data));
    }, []);

    return (
        <div className="p-8">
            <h2 className="text-3xl font-bold mb-6">Execution History</h2>
            <div className="bg-surface rounded-xl border border-slate-700 overflow-hidden">
                <table className="w-full text-left border-collapse">
                    <thead>
                        <tr className="bg-slate-800 text-slate-400 border-b border-slate-700">
                            <th className="p-4">ID</th>
                            <th className="p-4">Request</th>
                            <th className="p-4">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {tasks.map((t: any) => (
                            <tr key={t.id} className="border-b border-slate-700/50">
                                <td className="p-4">{t.id}</td>
                                <td className="p-4">{t.userRequest}</td>
                                <td className="p-4">{t.status}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
""",
    "ToolRegistryView.tsx": """import { useState, useEffect } from 'react';
import axios from 'axios';

export default function ToolRegistryView() {
    const [tools, setTools] = useState<any[]>([]);
    
    useEffect(() => {
        axios.get('http://localhost:8080/api/data/tools').then(res => setTools(res.data));
    }, []);

    return (
        <div className="p-8">
            <h2 className="text-3xl font-bold mb-6">Tool Registry</h2>
            <div className="grid grid-cols-3 gap-6">
                {tools.map((t: any) => (
                    <div key={t.name} className="bg-surface p-6 rounded-xl border border-slate-700">
                        <h3 className="font-bold text-lg text-brand-400 mb-2">{t.name}</h3>
                        <p className="text-slate-400 text-sm mb-4">{t.description}</p>
                        <div className="flex gap-2 text-xs">
                            <span className="bg-slate-800 px-2 py-1 rounded">Role: {t.requiredRole}</span>
                            <span className={`px-2 py-1 rounded ${t.riskLevel === 'HIGH' ? 'bg-red-500/20 text-red-500' : 'bg-green-500/20 text-green-500'}`}>Risk: {t.riskLevel}</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
""",
    "ArchitectureView.tsx": """export default function ArchitectureView() {
    return (
        <div className="p-8 max-w-4xl">
            <h2 className="text-3xl font-bold mb-6">Architecture Diagram</h2>
            <div className="bg-surface p-8 rounded-xl border border-slate-700 space-y-6">
                <div className="flex flex-col items-center gap-4 text-center">
                    <div className="bg-brand-900/50 border border-brand-500/50 p-4 rounded-lg w-64">
                        <h3 className="font-bold text-brand-400">React Frontend</h3>
                        <p className="text-xs text-slate-400 mt-1">User Interface & Chat</p>
                    </div>
                    <div className="h-8 w-px bg-slate-600"></div>
                    <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-64">
                        <h3 className="font-bold">Spring Boot API</h3>
                        <p className="text-xs text-slate-400 mt-1">REST Controllers</p>
                    </div>
                    <div className="h-8 w-px bg-slate-600"></div>
                    <div className="flex gap-4">
                        <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-48">
                            <h3 className="font-bold">Agent Service</h3>
                            <p className="text-xs text-slate-400 mt-1">State Machine & Logic</p>
                        </div>
                        <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-48">
                            <h3 className="font-bold">Tool Registry</h3>
                            <p className="text-xs text-slate-400 mt-1">Controlled Actions</p>
                        </div>
                    </div>
                    <div className="h-8 w-px bg-slate-600"></div>
                    <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-64">
                        <h3 className="font-bold">SQLite Database</h3>
                        <p className="text-xs text-slate-400 mt-1">State, Logs, Tickets</p>
                    </div>
                </div>
            </div>
        </div>
    );
}
""",
    "WorkflowView.tsx": """export default function WorkflowView() {
    return (
        <div className="p-8 max-w-4xl">
            <h2 className="text-3xl font-bold mb-6">Agent Workflow</h2>
            <div className="bg-surface p-8 rounded-xl border border-slate-700">
                <ul className="space-y-4 font-mono text-sm">
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-slate-500">RECEIVED -> Request received from user</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-slate-500">ANALYZING -> Determine intent</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-slate-500">PLANNING -> Select tool</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-yellow-500">WAITING_FOR_AUTHORIZATION -> (If HIGH risk)</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-brand-500">EXECUTING -> Run tool via registry</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-brand-500">VALIDATING -> Check output</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-green-500">COMPLETED -> Return to user</li>
                </ul>
            </div>
        </div>
    );
}
""",
    "DeploymentView.tsx": """export default function DeploymentView() {
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
""",
    "SecurityView.tsx": """export default function SecurityView() {
    return (
        <div className="p-8 max-w-4xl">
            <h2 className="text-3xl font-bold mb-6">Security Model</h2>
            <div className="bg-surface p-8 rounded-xl border border-slate-700 space-y-4">
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">1. Role-Based Access Control</h3>
                    <p className="text-sm text-slate-400 mt-1">Users have USER, SUPPORT_AGENT, or ADMIN roles. Tools are restricted by role.</p>
                </div>
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">2. Human-in-the-Loop</h3>
                    <p className="text-sm text-slate-400 mt-1">High-risk tools (like close_ticket) pause execution and require explicit ADMIN approval.</p>
                </div>
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">3. Indirect Database Access</h3>
                    <p className="text-sm text-slate-400 mt-1">The agent cannot execute arbitrary SQL. It only has access to predefined tools in the Tool Registry.</p>
                </div>
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">4. Audit Logging</h3>
                    <p className="text-sm text-slate-400 mt-1">All agent actions and tool executions are persistently logged for compliance.</p>
                </div>
            </div>
        </div>
    );
}
""",
    "MonitoringView.tsx": """export default function MonitoringView() {
    return (
        <div className="p-8">
            <h2 className="text-3xl font-bold mb-6">Monitoring Dashboard</h2>
            <div className="grid grid-cols-4 gap-6 mb-6">
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">System Status</div>
                    <div className="text-2xl font-bold text-green-400">HEALTHY</div>
                </div>
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">Total Tasks</div>
                    <div className="text-2xl font-bold text-brand-400">14</div>
                </div>
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">Pending Approvals</div>
                    <div className="text-2xl font-bold text-yellow-400">1</div>
                </div>
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">AI Mode</div>
                    <div className="text-2xl font-bold text-blue-400">DEMO (Rule-Based)</div>
                </div>
            </div>
        </div>
    );
}
"""
}

for name, content in views.items():
    with open(os.path.join(base_dir, name), "w") as f:
        f.write(content)

print("Remaining views created.")
