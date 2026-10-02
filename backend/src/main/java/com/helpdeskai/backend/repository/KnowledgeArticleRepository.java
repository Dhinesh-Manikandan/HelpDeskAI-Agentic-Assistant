package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.KnowledgeArticle;
import org.springframework.data.jpa.repository.JpaRepository;
public interface KnowledgeArticleRepository extends JpaRepository<KnowledgeArticle, Long> {
}