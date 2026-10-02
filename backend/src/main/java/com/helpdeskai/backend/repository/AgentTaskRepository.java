package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.AgentTask;
import org.springframework.data.jpa.repository.JpaRepository;
public interface AgentTaskRepository extends JpaRepository<AgentTask, Long> {
}