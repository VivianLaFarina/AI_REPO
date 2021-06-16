package jorge.cardona.concepts.service;

import jorge.cardona.concepts.entity.NatureEntity;
import jorge.cardona.concepts.repository.NatureInterfaceRepository;
import jorge.cardona.concepts.repository.NatureRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class NatureService implements NatureInterfaceRepository {

    @Autowired
    NatureRepository natureRepository;

    public List<NatureEntity> getNatureList() {
        return natureRepository.findAll();
    }

    public Optional<NatureEntity> getNatureById(UUID id) {
        return natureRepository.findById(id);
    }


    public NatureEntity saveNature(NatureEntity natureEntity) {

        return natureRepository.save(natureEntity);
    }

    public List<NatureEntity> saveListNature(List<NatureEntity> natureEntity) {

        return natureRepository.saveAll(natureEntity);
    }
}
