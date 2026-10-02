import { useState, useEffect } from 'react';
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
