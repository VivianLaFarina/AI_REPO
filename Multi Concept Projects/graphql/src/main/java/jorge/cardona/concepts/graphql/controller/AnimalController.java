package jorge.cardona.concepts.graphql.controller;

import io.leangen.graphql.annotations.GraphQLArgument;
import io.leangen.graphql.annotations.GraphQLMutation;
import io.leangen.graphql.annotations.GraphQLQuery;
import io.leangen.graphql.spqr.spring.annotations.GraphQLApi;
import jorge.cardona.concepts.graphql.dto.AnimalDTO;
import jorge.cardona.concepts.graphql.entity.AnimalEntity;
import jorge.cardona.concepts.graphql.mapper.AnimalMapper;
import jorge.cardona.concepts.graphql.repository.AnimalRepository;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
@GraphQLApi
@AllArgsConstructor
public class AnimalController {

    @Autowired
    private final AnimalRepository animalRepository;

    @Autowired
    private final AnimalMapper animalMapper;

    @GraphQLQuery(name = "animals") // READ ALL
    public Iterable<AnimalDTO> getAnimals() {

        return animalMapper.listAnimalEntityToDto((List<AnimalEntity>) animalRepository.findAll());
    }

    @GraphQLQuery(name = "animal") // READ BY ID
    public AnimalDTO getAnimalById(@GraphQLArgument(name = "id") Long id) {

        return animalMapper.animalEntityToDto(animalRepository.findById(id).get());
    }

    @GraphQLMutation(name = "saveAnimal") // CREATE
    public AnimalEntity saveAnimal(@GraphQLArgument(name = "animal") AnimalEntity animalEntity) {
        return animalRepository.save(animalEntity);
    }

    @GraphQLMutation(name = "saveAnimalList") // CREATE LIST
    public Iterable<AnimalEntity> saveAnimalList(@GraphQLArgument(name = "animalList") List<AnimalEntity> animalEntityList) {
        return animalRepository.saveAll(animalEntityList);
    }

    @GraphQLMutation(name = "deleteAnimal") // DELETE
    public void deleteAnimal(@GraphQLArgument(name = "id") Long id) {
        animalRepository.deleteById(id);
    }

    @GraphQLQuery(name = "isFriendly") // Calculated property of animal
    public boolean tender(@GraphQLArgument(name = "friend") AnimalEntity animalEntity) {
        return !Arrays.asList("Shark", "Snake").contains(animalEntity.getName());
    }
}