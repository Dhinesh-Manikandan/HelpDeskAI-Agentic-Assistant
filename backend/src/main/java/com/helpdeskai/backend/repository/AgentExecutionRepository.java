package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.AgentExecution;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
public interface AgentExecutionRepository extends JpaRepository<AgentExecution, Long> {
    List<AgentExecution> findByTaskIdOrderByIdDesc(Long taskId);
    List<AgentExecution> findByTaskIdOrderByIdAsc(Long taskId);
}